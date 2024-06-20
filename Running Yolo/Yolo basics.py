from ultralytics import YOLO
import cv2

model = YOLO('../Yolo-Weights/yolov8l.pt')
result = model('F:\PRO\Running Yolo\istockphoto-1338736300-612x612.jpg', show=True)
cv2.waitKey(0)
