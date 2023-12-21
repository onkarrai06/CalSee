from ultralytics import YOLO
from calculate import calcuate_dim
import cv2
from PIL import Image
import numpy as np
from knn.knn import predict_calories
from yolo.preprocessing import preprocess_image

WEIGHTS = 'D:\Class\DIP\projecGithub\CalSee\DIPv1\yolo\yolov8n7\weights\last.pt'

def predict(top_img, side_img):
    
    """
    top_img = cv2.imread(top_img)
    side_img = cv2.imread(side_img)
    """
    top_img = Image.open(top_img)
    top_img = np.array(top_img)

    side_img = Image.open(side_img)
    side_img = np.array(side_img)

    top_img = cv2.cvtColor(top_img, cv2.COLOR_RGB2BGR)
    side_img = cv2.cvtColor(side_img, cv2.COLOR_RGB2BGR)

    top_img = preprocess_image(top_img)
    side_img = preprocess_image(side_img)
    
    # Load model
    model = YOLO(WEIGHTS)
    classes = model.names

    top_result = model(top_img)
    side_result = model(side_img)

    top_boxes = top_result[0].boxes.cpu().numpy()
    side_boxes = side_result[0].boxes.cpu().numpy()

    top_list_of_objects = []
    side_list_of_objects = []
    
    for box in top_boxes:
        dim = box.xywh
        x,y,w,h = dim[0][0],dim[0][1],dim[0][2],dim[0][3]
        obj = int(box.cls[0])
        top_list_of_objects.append([obj,x,y,w,h])
        cv2.rectangle(top_img,(int(x-w/2),int(y-h/2)),(int(x+w/2),int(y+h/2)),(255,0,0),2)
        cv2.putText(top_img,classes[obj],(int(x),int(y)),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)

    for box in side_boxes:
        dim = box.xywh
        x,y,w,h = dim[0][0],dim[0][1],dim[0][2],dim[0][3]
        obj = int(box.cls[0])
        print(classes[obj])
        side_list_of_objects.append([obj,x,y,w,h])

        cv2.rectangle(side_img,(int(x-w/2),int(y-h/2)),(int(x+w/2),int(y+h/2)),(255,0,0),2)
        cv2.putText(side_img,classes[obj],(int(x),int(y)),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)
        
    top_dim = calcuate_dim(top_list_of_objects)
    side_dim = calcuate_dim(side_list_of_objects)

    results = []
    for i in range(len(top_dim)):
        
        top_area = top_dim[i][1] * top_dim[i][2]
        side_area = side_dim[i][1] * side_dim[i][2]
        calories = predict_calories(top_dim[i][0], side_area, top_area)
        
        obj = classes[top_dim[i][0]]

        results.append([obj,calories])
    
    """
    print(results)
    cv2.imshow('topimage',top_img)
    cv2.imshow('sideimage',side_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    """

    top_img = cv2.cvtColor(top_img, cv2.COLOR_BGR2RGB)
    side_img = cv2.cvtColor(side_img, cv2.COLOR_BGR2RGB)
    return results, top_img, side_img
    
#predict("D:\Class\DIP\projecGithub\CalSee\DIPv1\\testimages\\test_image.JPG","D:\Class\DIP\projecGithub\CalSee\DIPv1\\testimages\\1bananasT.jpeg")
