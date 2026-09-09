from ultralytics import YOLO

model = YOLO("runs/detect/train/weights/best.pt")

results = model("dataset/images/val/gss1007_jpg.rf.efc15b26b138ce05cd67dacceade4d3a.jpg", save=True)

print("Testing complete!")