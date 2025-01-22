from ultralytics import YOLO

# Create a new YOLO model from scratch
model = YOLO("yolo11n-seg.yaml")  # build a new model from YAML

# Load a pretrained YOLO model (recommended for training)
model = YOLO("yolo11n-seg.pt")  # load a pretrained model (recommended for training)

# Train the model using the 'coco8.yaml' dataset for 3 epochs
results = model.train(data="coco8-seg.yaml", epochs=100, imgsz=640)

# Evaluate the model's performance on the validation set
results = model.val()

# Perform object detection on an image using the model
results = model("https://ultralytics.com/images/bus.jpg")

# https://docs.ultralytics.com/zh/quickstart/#inspecting-settings

# Export the model to ONNX format
success = model.export(format="onnx")