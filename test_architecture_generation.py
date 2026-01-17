from app.reasoning.gemini_architect import generate_architecture

flow_data = {
	"screen": "Login",
	"flows": [
		"Login -> Signup",
		"Login -> Home"
	]
}

result = generate_architecture(flow_data)
print(result)
