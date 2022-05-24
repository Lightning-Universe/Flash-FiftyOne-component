import logging
from typing import Any, Dict

from lightning import LightningFlow
from lightning.storage.path import Path

from flash_fiftyone.flash_fiftyone_work import FlashFiftyOneWork


class FlashFiftyOne(LightningFlow):
    def __init__(self):
        super().__init__()

        self.work = FlashFiftyOneWork()
        self.run_id = None
        self.url = None

        self.ready = False

    def run(self, run_id: int, task: str, url: str, data_config: Dict, checkpoint: Path):
        self.ready = False

        if self.run_id != run_id:
            logging.info(
                f"Launching FiftyOne with path: {checkpoint}, of type: {type(checkpoint)}"
            )
            self.run_id = run_id
            self.work.run(task, url, data_config, checkpoint)

        if self.work.has_succeeded:
            self.ready = True
            self.url = self.work.url

