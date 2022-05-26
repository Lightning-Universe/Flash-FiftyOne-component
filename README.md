<div align="center">
<img src="https://pl-bolts-doc-images.s3.us-east-2.amazonaws.com/lai.png" width="200px">

A Lightning component to serve a Flash Task using FiftyOne

______________________________________________________________________

</div>

## Use the component

Note that we have a `run_once` argument to the component, this allows you to only run it once if needed. Default is `True`, which means it will only run once if not set `False` explicitly.

```python
import lightning as L
from lightning import LightningApp

from flash_fiftyone import FlashFiftyOne


class FiftyOneComponent(L.LightningFlow):
    def __init__(self):
        super().__init__()
        # We only run FlashFiftyOne once, since we only have one input
        # default for `run_once` is `True` as well
        self.flash_fiftyone = FlashFiftyOne(run_once=True)
        self.layout = []

    def run(self):
        # Pass a checkpoint path for FiftyOne to load
        checkpoint_path = "checkpoint.pt"

        run_dict = {
            "id": 0,
            "task": "image_classification",
            "url": "https://pl-flash-data.s3.amazonaws.com/hymenoptera_data.zip",
            "data_config": {
                "target": "from_folders",
                "train_folder": "hymenoptera_data/train/",
                "val_folder": "hymenoptera_data/val/",
            },
        }

        self.flash_fiftyone.run(
            run_dict["task"],
            run_dict["url"],
            run_dict["data_config"],
            checkpoint_path,
        )

    def configure_layout(self):
        if self.flash_fiftyone.ready and not self.layout:
            self.layout.append(
                {
                    "name": "Predictions Explorer (FiftyOne)",
                    "content": self.flash_fiftyone,
                },
            )
        return self.layout


# To launch the fiftyone component
app = LightningApp(FiftyOneComponent(), debug=True)
```

## Install

Use these instructions to install:

```bash
git clone https://github.com/PyTorchLightning/LAI-flash-fiftyone.git
cd LAI-flash-fiftyone
pip install -r requirements.txt
pip install -e .
```
