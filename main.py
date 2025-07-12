"""
Object Detection System using YOLOv5
Internship Project for CodeClause - July 2025
Author: Raman Kumar

This script performs real-time object detection using a webcam feed.
It uses the YOLOv5m model from the Ultralytics library and is optimized
for CPU performance by resizing frames and skipping alternate frames.
"""
from ultralytics import YOLO
import cv2

# ------------------- Load the YOLOv5 Model -------------------
# Load a medium-sized model for better accuracy (more than yolov5s)
model = YOLO("yolov5m.pt")

# ------------------- Start Webcam -------------------
# Open the default webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

print("Press 'q' to quit.")
frame_id = 0  # For skipping frames

# ------------------- Real-Time Detection Loop -------------------
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Optional: Resize to speed up detection
    frame = cv2.resize(frame, (640, 480))

    # Skip every other frame for smoother performance
    frame_id += 1
    if frame_id % 2 != 0:
        continue

    # Run detection
    results = model(frame, stream=True)

    # Draw results on frame
    for r in results:
        for box in r.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])  # Bounding box
            conf = box.conf[0]
            cls = int(box.cls[0])
            label = model.names[cls]

            # Draw rectangle & label
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, f"{label} {conf:.2f}", (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    # Show the frame
    cv2.imshow("Object Detection - Webcam (Optimized)", frame)

    # Exit on 'q'
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# ------------------- Cleanup -------------------
cap.release()
cv2.destroyAllWindows()

# Note: Press 'q' while focused on the video window to exit the program.