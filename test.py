from ultralytics import YOLO
model = YOLO('runs/detect/train12/weights/best.pt')
results = model(r"D:\Object Detection\images\test\DSC_0968.JPG", save=True, conf=0.25)

# Show or inspect results
results[0].show()  # display in notebook (if using Jupyter)
results[0].save(filename='output.jpg')  # save to file (optional)