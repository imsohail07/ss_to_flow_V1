from app.vision.ui_detector import UIDetector

detector=UIDetector("yolov8n.pt")

elements, output=detector.detect("uploads/signup.png")

print("Detected UI Elements:")
for e in elements:
	print(e)

print("\nAnnotated image saved at:", output)
