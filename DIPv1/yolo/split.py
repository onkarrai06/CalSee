import os
import random
import shutil

TRAIN = 0.8
TEST = 0.2


def train_test_split():

    # getting all images
    DATASET = os.listdir(".\DIPv1\yolo\dataset\images")
    random.shuffle(DATASET)

    #Image Directories
    os.makedirs("./DIPv1/yolo/dataset/images/train") if not os.path.exists(
        "./DIPv1/yolo/dataset/images/train"
    ) else None
    os.makedirs("./DIPv1/yolo/dataset/images/test") if not os.path.exists(
        "./DIPv1/yolo/dataset/images/test"
    ) else None
    os.makedirs("./DIPv1/yolo/dataset/images/validation") if not os.path.exists(
        "./DIPv1/yolo/dataset/images/validation"
    ) else None

    #Label Directiroies
    os.makedirs("./DIPv1/yolo/dataset/labels/train") if not os.path.exists(
        "./DIPv1/yolo/dataset/labels/train"
    ) else None
    os.makedirs("./DIPv1/yolo/dataset/labels/test") if not os.path.exists(
        "./DIPv1/yolo/dataset/labels/test"
    ) else None
    os.makedirs("./DIPv1/yolo/dataset/labels/validation") if not os.path.exists(
        "./DIPv1/yolo/dataset/labels/validation"
    ) else None

    # training and testing data indexs
    train_size = int(len(DATASET) * TRAIN)
    test_size = int(len(DATASET) * TEST)
    print(train_size)
    print(test_size)

    # splitting data
    train_set = DATASET[:train_size]
    test_set = DATASET[train_size:]

    # validation set
    validation_set = test_set[: test_size // 2]
    test_set = test_set[test_size // 2 :]

    # moving images to respective folders
    for image in train_set:
        shutil.move(
            ".\DIPv1\yolo\dataset\images\\" + image,
            ".\DIPv1\yolo\dataset\images\\train\\" + image,
        )
        shutil.move(
            ".\DIPv1\yolo\dataset\labels\\" + image[:-4] + ".txt",
            ".\DIPv1\yolo\dataset\labels\\train\\" + image[:-4] + ".txt",
        )

    for image in test_set:
        shutil.move(
            ".\DIPv1\yolo\dataset\images\\" + image,
            ".\DIPv1\yolo\dataset\images\\test\\" + image,
        )
        shutil.move(
            ".\DIPv1\yolo\dataset\labels\\" + image[:-4] + ".txt",
            ".\DIPv1\yolo\dataset\labels\\test\\" + image[:-4] + ".txt",
        )
    
    for image in validation_set:
        shutil.move(
            ".\DIPv1\yolo\dataset\images\\" + image,
            ".\DIPv1\yolo\dataset\images\\validation\\" + image,
        )
        shutil.move(
            ".\DIPv1\yolo\dataset\labels\\" + image[:-4] + ".txt",
            ".\DIPv1\yolo\dataset\labels\\validation\\" + image[:-4] + ".txt",
        )