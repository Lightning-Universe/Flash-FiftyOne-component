from flash_fiftyone import FlashFiftyOne


def test_flash_fiftyone_image_classification():
    # TODO: Maybe use mock for checkpoint
    # Worst case: have a minimal checkpoint
    checkpoint_path = "checkpoint.pt"

    # Sample run data config to test workflow
    run_dict = {
        "id": 0,
        "task": "image_classification",
        # TODO: Maybe have a smaller dataset for test?
        "url": "https://pl-flash-data.s3.amazonaws.com/hymenoptera_data.zip",
        "data_config": {
            "target": "from_folders",
            "train_folder": "hymenoptera_data/train/",
            "val_folder": "hymenoptera_data/val/",
        },
    }

    flash_fiftyone = FlashFiftyOne()
    result = flash_fiftyone.run(
        run_dict,
        checkpoint_path,
    )
    assert result.status_code == 200
