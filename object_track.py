import ultralytics 
from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt", "v8")

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()

    if not ret:
        print("{ret}->camera fail to open")

    result = model.track(frame, persist=True)

    visual=result[0].plot()

    cv2.imshow("object tracking", visual)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()