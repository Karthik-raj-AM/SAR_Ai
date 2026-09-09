from ultralytics import YOLO
import cv2

model = YOLO("yolo11n.pt")

image = cv2.imread("test.jpg")

results = model(image)

for result in results:
    for box in result.boxes:

        confidence = box.conf.item()
        class_id = int(box.cls.item())

        if class_id == 0 and confidence > 0.5:

            x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())

            center_x = (x1 + x2) // 2
            center_y = (y1 + y2) // 2

            # Draw bounding box
            cv2.rectangle(
                image,
                (x1, y1),
                (x2, y2),
                (255, 0, 0),
                2
            )

            # Write information
            text = f"SURVIVOR {confidence * 100:.1f}%"

            cv2.putText(
                image,
                text,
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (255, 0, 0),
                2
            )

            # Draw center point
            cv2.circle(
                image,
                (center_x, center_y),
                5,
                (0, 0, 255),
                -1
            )

            print("🚨 SURVIVOR DETECTED")
            print("Confidence:", round(confidence * 100, 1), "%")
            print("Position:", center_x, center_y)

cv2.imshow("SAR AI", image)

cv2.waitKey(0)
cv2.destroyAllWindows()