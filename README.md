<div align="center">
<img src="https://pl-bolts-doc-images.s3.us-east-2.amazonaws.com/lai.png" width="200px">

A Lightning component to serve a Flash Task using FiftyOne

______________________________________________________________________

</div>

## Install

Use these instructions to install:

```bash
git clone https://github.com/Lightning-AI/LAI-flash-fiftyone-Component.git
cd LAI-flash-fiftyone-Component
pip install -r requirements.txt
pip install -e .
```

## Use the component

**Note:**

1. We have a `cache_calls` argument to the component, this allows you to only run it only once as long as same arguments are passed to the `run` method of `FlashFiftyOne` class.
1. This component currently only supports `task` as `image_classification`. Please make sure to pass `"task": "image_classification"` in the `run_dict` as shown below.

To run the code below, copy the code and save it in a file `app.py`. Run the component using `lightning run app app.py`. If you want to run the app on cloud, do: `lightning run app app.py --cloud`.

```python
import lightning as L

from flash_fiftyone import FlashFiftyOne


class FiftyOneComponent(L.LightningFlow):
    def __init__(self):
        super().__init__()
        self.flash_fiftyone = FlashFiftyOne(cache_calls=True)
        self.layout = []

    def run(self):
        # Pass your data here:
        # `task` can be either image_classification or text_classification
        # `url` needs to be a downloadable link for your dataset
        # Depending on the task you've chosen, pass the arguments to the task class
        #   from Lightning Flash in the `data_config` dict
        # `checkpoint_path` can either be a local path to the checkpoint or any hosted link
        run_dict = {
            "task": "image_classification",
            "url": "https://pl-flash-data.s3.amazonaws.com/hymenoptera_data.zip",
            "data_config": {
                "target": "from_folders",
                "train_folder": "hymenoptera_data/train/",
                "val_folder": "hymenoptera_data/val/",
            },
            "checkpoint_path": "https://flash-weights.s3.amazonaws.com/0.7.0/image_classification_model.pt",
        }

        self.flash_fiftyone.run(
            task=run_dict["task"],
            url=run_dict["url"],
            data_config=run_dict["data_config"],
            checkpoint_path=run_dict["checkpoint_path"],
        )

    def configure_layout(self):
        # Use flash_fiftyone.ready flag - which will be `True` when fiftyone server is ready and the task is served!
        if self.flash_fiftyone.ready and not self.layout:
            self.layout.append(
                {
                    "name": "Predictions Explorer (FiftyOne)",
                    "content": self.flash_fiftyone,
                },
            )
        return self.layout


app = L.LightningApp(FiftyOneComponent(), debug=True)
```
