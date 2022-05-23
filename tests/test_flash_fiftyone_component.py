from flash_fiftyone import FlashFiftyOne


# TODO: add a test for text classification
def test_flash_fiftyone_image_classification():
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

    flash_fiftyone = FlashFiftyOne()
    result = flash_fiftyone.run(run_dict, checkpoint_path)
    assert result.status_code == 200
