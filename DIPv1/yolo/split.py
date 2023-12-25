import os
import random
import shutil
import cv2
from preprocessing import preprocess_image

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
    
    coins_train_images = os.listdir("DIPv1\coin\\train\images")    
    coins_validation_images = os.listdir("DIPv1\coin\\valid\images")

    random.shuffle(coins_validation_images)
    coins_test_images = coins_validation_images[:len(coins_validation_images) // 2]
    coins_validation_images = coins_validation_images[len(coins_validation_images) // 2:]

    for path in coins_validation_images:

        image = cv2.imread(".\DIPv1\coin\\valid\images\\" + path)
        image = preprocess_image(image)
        
        cv2.imwrite(".\DIPv1\yolo\dataset\images\\validation\\" + path, image)

        shutil.copy(
            ".\DIPv1\coin\\valid\labels\\" + path[:-4] + ".txt",
            ".\DIPv1\yolo\dataset\labels\\validation\\" + path[:-4] + ".txt",
        )
    
    for path in coins_test_images:
        
        image = cv2.imread(".\DIPv1\coin\\valid\images\\" + path)
        image = preprocess_image(image)
        cv2.imwrite(".\DIPv1\yolo\dataset\images\\test\\" + path, image)
        
        shutil.copy(
            ".\DIPv1\coin\\valid\labels\\" + path[:-4] + ".txt",
            ".\DIPv1\yolo\dataset\labels\\test\\" + path[:-4] + ".txt",
        )
    
    for path in coins_train_images:
        
        image = cv2.imread(".\DIPv1\coin\\train\images\\" + path)
        image = preprocess_image(image)
        cv2.imwrite(".\DIPv1\yolo\dataset\images\\train\\" + path, image)

        shutil.copy(
            ".\DIPv1\coin\\train\labels\\" + path[:-4] + ".txt",
            ".\DIPv1\yolo\dataset\labels\\train\\" + path[:-4] + ".txt",
        )
    

train_test_split()