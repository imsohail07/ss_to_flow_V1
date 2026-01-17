from ultralytics import YOLO
import cv2
import os

class UIDetector:
	def __init__(self, model_path="yolov8n.pt"):
		self.model=YOLO(model_path)

	def detect(self, image_path, save_dir="runs/ui_detection"):
		os.makedirs(save_dir, exist_ok=True)

		results=self.model(image_path)

		img=cv2.imread(image_path)

		ui_elements=[]

		for r in results:
			for box in r.boxes:
				x1,y1,x2,y2=map(int, box.xyxy[0])
				conf=float(box.conf[0])
				cls=int(box.cls[0])
				label=self.model.names[cls]

				ui_elements.append({
					"label":label,
					"confidence":round(conf,2),
					"bbox":[x1,y1,x2,y2]
				})

				cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
				cv2.putText(img,label,(x1,y1-10),
					cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),2)

		output_path=os.path.join(save_dir,"annotated.png")
		cv2.imwrite(output_path,img)

		return ui_elements, output_path
