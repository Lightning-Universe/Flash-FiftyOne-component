from flash_fiftyone import FlashFiftyOne


def test_flash_fiftyone_image_classification():
    # Sample run data config to test workflow
    run_dict = {
        "task": "image_classification",
        # TODO: Maybe have a smaller dataset for test?
        "url": "https://pl-flash-data.s3.amazonaws.com/hymenoptera_data.zip",
        "data_config": {
            "target": "from_folders",
            "train_folder": "hymenoptera_data/train/",
            "val_folder": "hymenoptera_data/val/",
        },
        "checkpoint_path": "https://flash-weights.s3.amazonaws.com/0.7.0/image_classification_model.pt",
    }

    flash_fiftyone = FlashFiftyOne()
    flash_fiftyone.run(
        task=run_dict["task"],
        url=run_dict["url"],
        data_config=run_dict["data_config"],
        checkpoint_path=run_dict["checkpoint_path"],
    )
    assert flash_fiftyone.ready
