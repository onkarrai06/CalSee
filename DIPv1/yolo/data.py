import os
import xml.etree.ElementTree as ET
import numpy as np
import cv2
from split import train_test_split
from create_yaml import yaml_create
from preprocessing import preprocess_image

path = ".\DIPv1\ECUSTFD-resized--master"

if os.path.exists(".\DIPv1\yolo\dataset"):
    os.system("rmdir /Q /S .\DIPv1\yolo\dataset")

# creating new dataset dir for yolo
create_dir = os.makedirs(".\DIPv1\yolo\dataset")
new_path = ".\DIPv1\yolo\dataset"

# creating a new folder for images and  annotations
create_dir = (
    os.makedirs(new_path + "\images")
    if not os.path.exists(new_path + "\images")
    else None
)
create_dir = (
    os.makedirs(new_path + "\\labels")
    if not os.path.exists(new_path + "\\labels")
    else None
)

class_dict = {}

#list of classes and index being the ids
classes = ["coin"]
image_files = os.listdir(path + "\JPEGImages")


for elem in os.listdir(path + "\Annotations"):
    
    #parsing xml file
    inpath = path + "\Annotations\\" + elem
    tree = ET.parse(inpath)
    root = tree.getroot()

    #getting image name
    filename = root.find("./filename").text
    if filename not in image_files:
        print(filename + " not found, skipping...")
        continue
    
    #reading image
    image = cv2.imread(path + "\JPEGImages\\" + filename)
    #getting image dimensions
    height, width, band = image.shape

    #prepocessing image
    image = preprocess_image(image)
    
    #saving image
    cv2.imwrite(new_path + "\images\\" + filename, image)
    
    #annotations
    txt_file = open(new_path + "\\labels\\" + filename[0:-4] + ".txt", "w")

    for child in root:
        img_annotation = []
        if child.tag == "object":
            
            #recording the class and getting a class id
            img_annotation_class = child.find("./name").text

            if img_annotation_class != "coin":
                if img_annotation_class in class_dict:
                    class_dict[img_annotation_class].append(filename)
                else:
                   class_dict[img_annotation_class] = [filename]

            if img_annotation_class not in classes:
                classes.append(img_annotation_class)
            class_index = classes.index(img_annotation_class)
            
            #getting the bounding box coordinates
            xmin = int(child.find("./bndbox/xmin").text)
            ymin = int(child.find("./bndbox/ymin").text)
            xmax = int(child.find("./bndbox/xmax").text)
            ymax = int(child.find("./bndbox/ymax").text)

            #converting to yolo format
            x_center = (xmin + xmax) / 2 / width
            y_center = (ymin + ymax) / 2 / height
            w = (xmax - xmin) / width
            h = (ymax - ymin) / height
        
            #appending to the list
            img_annotation.append([class_index, x_center, y_center, w, h])

            #saving the annotations
            for line in img_annotation:
                txt_file.write(" ".join(str(x) for x in line) + "\n")

    #close file
    txt_file.close()
    
#saving the list of classes with the corresponding rows being the id (startin at 0)
with open(".\DIPv1\classes.txt", "w") as f:
    f.write("\n".join(classes))

train_test_split()

yaml_create()