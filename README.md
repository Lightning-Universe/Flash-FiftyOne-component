<div align="center">
<img src="https://pl-bolts-doc-images.s3.us-east-2.amazonaws.com/lai.png" width="200px">

A Lightning component to serve a Flash Task using FiftyOne
______________________________________________________________________

</div>

## Use the component

```python
from typing import Any, Dict

import lightning as L
from lightning.storage.path import Path

from flash_fiftyone import FlashFiftyOne

class YourComponent(L.LightningFlow):
  def __init__(self):
    super().__init__()
    self.flash_fiftyone = FlashFiftyOne()

  def run(self, run: dict, checkpoint_path):
    # Pass a checkpoint path for FiftyOne to load
    checkpoint_path = "sampleCheckpoint.pth"
    # TODO: example will be complex if we mention how to retrieve this run dict
    self.flash_fiftyone.run(
      run_dict,
      checkpoint_path,
    )
```

## Install

Use these instructions to install:

```bash
git clone https://github.com/PyTorchLightning/LAI-flash-fiftyone.git
cd LAI-flash-fiftyone
pip install -r requirements.txt
pip install -e .
```
