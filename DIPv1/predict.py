from ultralytics import YOLO
from calculate import calcuate_dim

WEIGHTS = 'CalSee\DIPv1\yolov8n7\weights\\best.pt'

def predict(source):
    # Load model
    model = YOLO(WEIGHTS)
    classes = model.names

    result = model(source)

    boxes = result[0].boxes.cpu().numpy()
    list_of_objects = [] 
    for box in boxes:

        dim = box.xywh
        x,y,w,h = dim[0][0],dim[0][1],dim[0][2],dim[0][3]
        obj = classes[int(box.cls[0])]
        list_of_objects.append([obj,x,y,w,h])

    print(list_of_objects)
    dim = calcuate_dim(list_of_objects)
    print(dim)

predict("CalSee\DIPv1\dataset\images\\test\\bread001T(3).JPG")