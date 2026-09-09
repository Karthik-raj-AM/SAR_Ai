from ultralytics import YOLO
import cv2

# Load YOLO
model = YOLO("yolo11n.pt")

# Open camera
camera = cv2.VideoCapture(0)

while True:

    success, frame = camera.read()

    if not success:
        print("Camera not working")
        break

    # Detect + track
    results = model.track(frame, persist=True)

    for result in results:

        for box in result.boxes:

            confidence = float(box.conf[0])
            class_id = int(box.cls[0])

            # Ignore weak detections
            if confidence < 0.5:
                continue

            # Object name
            object_name = model.names[class_id]

            # Bounding box
            x1, y1, x2, y2 = map(
                int,
                box.xyxy[0].tolist()
            )

            # Tracking ID
            if box.id is not None:
                track_id = int(box.id[0])
            else:
                track_id = 0

            # Person detected
            if class_id == 0:

                label = (
                    f"SURVIVOR "
                    f"ID:{track_id} "
                    f"{confidence * 100:.1f}%"
                )

                print(
                    f"SURVIVOR | "
                    f"ID:{track_id} | "
                    f"{confidence * 100:.1f}%"
                )

            else:

                label = (
                    f"{object_name} "
                    f"{confidence * 100:.1f}%"
                )

            # Draw bounding box
            cv2.rectangle(
                frame,
                (x1, y1),
                (x2, y2),
                (255, 0, 0),
                2
            )

            # Draw label
            cv2.putText(
                frame,
                label,
                (x1, max(y1 - 10, 20)),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (255, 0, 0),
                2
            )

    # Show camera
    cv2.imshow("SAR AI - TRACKING", frame)

    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()