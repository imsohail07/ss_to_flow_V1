import cv2
from app.vision.ui_detector import UIDetector
from app.flow.flow_infer import infer_screen_flow

detector = UIDetector("yolov8n.pt")

detections, _ = detector.detect("uploads/signup.png")

img = cv2.imread("uploads/signup.png")

flow = infer_screen_flow(detections, img.shape)

print("INFERRED SCREEN FLOW:\n")
print(flow)
