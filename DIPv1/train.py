import os
import sys
import xml.etree.ElementTree as ET
import json

path="ECUSTFD-resized--master\Annotations"

image = {}

for elem in os.listdir(path):

    inpath = path+"\\"+elem
    tree = ET.parse(inpath)
    root = tree.getroot()


    filename = root.find('./filename').text
    if filename not in image.keys():
        image[filename] = []


    for child in root:
        img = {}
        img["source"] =  "ECUSTFD-resized--master\JPEGImages"+"\\"+filename
        if child.tag == 'object':
            img["class"] = child.find('./name').text
            img["xmin"] = child.find('./bndbox/xmin').text
            img["ymin"] = child.find('./bndbox/ymin').text
            img["xmax"] = child.find('./bndbox/xmax').text
            img["ymax"] = child.find('./bndbox/ymax').text
            image[filename].append(img)

with open("dataset.json","w") as f:
        json.dump(image,f,indent=4)