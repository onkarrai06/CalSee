from ultralytics import YOLO
import torch

torch.cuda.set_device(0) # Set to your desired GPU number

device = torch.device("cuda:0")

def model(data_file, epochs, batch_size, verbose):
    model = YOLO('yolov8n.pt').to(device) # yolov5s.pt is automatically downloaded if not found
    
    model.train(data=data_file, epochs=epochs, batch=batch_size, verbose=verbose, project="F:\project", name="yolov8n", workers=2)
    metrics = model.val()
    
    path = model.export(format="onnx")
    
    return model

def run():
    torch.multiprocessing.freeze_support()
    print('loop')



if __name__ == "__main__":
    
    run()
    
    data_file = "data.yaml"
    epochs = 20
    batch_size = 16
    verbose = True
    
    model(data_file, epochs, batch_size, verbose)