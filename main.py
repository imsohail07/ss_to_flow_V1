from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import shutil
import os
import cv2

from app.vision.ui_detector import UIDetector
from app.flow.flow_infer import infer_screen_flow
from app.diagram.flow_diagram import generate_flow_diagram
from app.reasoning.gemini_architect import generate_architecture

app = FastAPI(title="Screenshot-to-Flow Agent")

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

detector = UIDetector("yolov8n.pt")


@app.get("/")
def home():
	return {"status": "Screenshot-to-Flow Agent is running"}

def root():
	return {"status":"server working"}


@app.post("/analyze-ui/")
async def analyze_ui(file: UploadFile = File(...)):
	file_path = os.path.join(UPLOAD_DIR, file.filename)

	with open(file_path, "wb") as buffer:
		shutil.copyfileobj(file.file, buffer)

	# 1. Detect UI components
	detections, annotated_path = detector.detect(file_path)

	# 2. Infer screen flow
	img = cv2.imread(file_path)
	flow_data = infer_screen_flow(detections, img.shape)

	# 3. Generate flow diagram
	diagram_path = generate_flow_diagram(flow_data, output_path="diagrams/user_flow")

	# 4. Generate architecture
	architecture = generate_architecture(flow_data)

	return JSONResponse({
		"message": "Analysis complete",
		"detections": detections,
		"flow": flow_data,
		"diagram": diagram_path + ".png",
		"architecture": architecture
	})
