def classify_screen(detections, image_shape):
	h, w, _ = image_shape

	# Heuristic: if big central container exists → it's a form-like screen
	if len(detections) <= 4:
		return "FormScreen"
	elif len(detections) > 6:
		return "ContentScreen"
	else:
		return "GenericScreen"


def infer_screen_flow(detections, image_shape):
	screen_type = classify_screen(detections, image_shape)

	screen = {
		"screen_name": screen_type,
		"components": [],
		"actions": []
	}

	# Register components
	for i, det in enumerate(detections):
		screen["components"].append({
			"id": f"component_{i}",
			"type": "UI_REGION",
			"bbox": det["bbox"]
		})

	# Generate generic actions
	if screen_type == "FormScreen":
		screen["actions"].append({
			"from": screen_type,
			"action": "SUBMIT_FORM",
			"to": "NextScreen"
		})
		screen["actions"].append({
			"from": screen_type,
			"action": "CANCEL_OR_BACK",
			"to": "PreviousScreen"
		})

	elif screen_type == "ContentScreen":
		screen["actions"].append({
			"from": screen_type,
			"action": "OPEN_ITEM",
			"to": "DetailScreen"
		})

	else:
		screen["actions"].append({
			"from": screen_type,
			"action": "NAVIGATE",
			"to": "AnotherScreen"
		})

	return screen
