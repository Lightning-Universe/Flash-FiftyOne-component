import os

from flash_fiftyone.component import FlashFiftyOne

__all__ = ["FlashFiftyOne"]

_PACKAGE_ROOT = os.path.dirname(__file__)
TEMPLATES_ROOT = os.path.join(_PACKAGE_ROOT, "templates")
