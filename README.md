# Screenshot-to-Flow Agent (Version 1)

## 📌 Overview

Screenshot-to-Flow Agent is a prototype AI system that attempts to **reverse engineer application UI flows from screenshots**.

The system takes a UI screenshot as input and automatically:

- Detects visual regions using computer vision
- Infers an abstract user flow
- Generates a flow diagram
- Suggests a frontend/backend project architecture

This is a **Version 1 prototype** focused on demonstrating the **end-to-end concept and pipeline**, not full semantic UI understanding.

---

## 🎯 Problem Statement

Reverse-engineering UI flows from screenshots is time-consuming for developers and designers. Teams must manually:

- Identify UI components
- Understand navigation structure
- Reconstruct screen-to-screen flows
- Design project folder structure

The goal of this project is to **automate the first-level understanding of UI screenshots** and produce:

- An abstract flow graph
- A visual diagram
- A suggested project architecture

---

## 🧠 What This System Does

1. Accepts a UI screenshot via API
2. Uses YOLOv8 to detect visual regions
3. Converts detected regions into abstract UI components
4. Uses rule-based flow inference to generate a navigation graph
5. Generates a flow diagram using Graphviz
6. Uses Gemini (with fallback) to suggest a project structure

---

## 🏗️ System Architecture

Screenshot
↓
YOLOv8 (visual region detection)
↓
Region → Abstract UI components
↓
Rule-based Flow Inference
↓
Flow Diagram Generator
↓
Architecture Suggestion (Gemini / Fallback)


## 🛠️ Tech Stack
- Python
- FastAPI
- YOLOv8 (Ultralytics)
- OpenCV
- Graphviz
- Gemini API (optional, with fallback)
- Swagger UI


API

POST /analyze-ui/

    Upload UI screenshot

    Returns:

        Detections
        Flow graph
        Diagram path
        Architecture suggestion

Current Limitations-

    Uses generic object detection (not UI-trained)
    No OCR yet
    Uses rule-based flow templates

Future Work-

    OCR integration

    UI semantic classification

    Multi-screen flow reconstruction

    UI dataset fine-tuning


---

# ✅ Step 3 — Create requirements.txt

Run:

pip freeze > requirements.txt

## 🚀 How to Run
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

python -m uvicorn main:app --reload



Then open:

http://127.0.0.1:8000/docs



