from ultralytics import YOLO

#load model
model = YOLO('yolov8n.pt')
results = model.train(data='config.yaml', epochs=100)

