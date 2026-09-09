from ultralytics import YOLO
from pathlib import Path

root = Path(__file__).resolve().parent


def main():
    model = YOLO(root / "yolo11n.pt")
    model.train(
        data=root / "dataset" / "data.yaml",
        epochs=50,
        imgsz=640,
        device=0,
        project=root / "runs" / "detect",
        name="train",
        exist_ok=True,
    )


if __name__ == "__main__":
    main()