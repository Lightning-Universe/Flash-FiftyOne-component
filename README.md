<div align="center">
<img src="https://pl-bolts-doc-images.s3.us-east-2.amazonaws.com/lai.png" width="200px">

A Lightning component to serve a Flash Task using FiftyOne

______________________________________________________________________

</div>

## Use the component

```python
import lightning as L
from lightning import LightningApp

from flash_fiftyone import FlashFiftyOne


class FiftyOneComponent(L.LightningFlow):
    def __init__(self):
        super().__init__()
        self.flash_fiftyone = FlashFiftyOne()

    def run(self):
        # Pass a checkpoint path for FiftyOne to load
        checkpoint_path = "checkpoint.pt"

        run_dict = {
            "task": "image_classification",
            "url": "https://pl-flash-data.s3.amazonaws.com/hymenoptera_data.zip",
            "data_config": {
                "target": "from_folders",
                "train_folder": "hymenoptera_data/train/",
                "val_folder": "hymenoptera_data/val/",
            },
        }

        self.flash_fiftyone.run(
            run_dict['task'],
            run_dict['url'],
            run_dict['data_config'],
            checkpoint_path,
        )

    def configure_layout(self):
        # Default cool spinner to show that it has not loaded yet!
        layout = [
            {
                "name": "Data Explorer (FiftyOne)",
                "content": "https://pl-flash-data.s3.amazonaws.com/assets_lightning/large_spinner.gif",
            }
        ]

        # Once the FlashFiftyOne component is ready
        if self.flash_fiftyone.ready:
            layout[0]["content"] = self.work.url
        return layout


# To launch the fiftyone component
app = LightningApp(YourComponent(), debug=True)
```

## Install

Use these instructions to install:

```bash
git clone https://github.com/PyTorchLightning/LAI-flash-fiftyone.git
cd LAI-flash-fiftyone
pip install -r requirements.txt
pip install -e .
```
