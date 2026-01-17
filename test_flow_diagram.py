from app.diagram.flow_diagram import generate_flow_diagram

flow_data = {
	"screen_name": "Login",
	"actions": [
		{"from": "Login", "action": "CLICK_SIGNUP", "to": "Signup"},
		{"from": "Login", "action": "SUBMIT_LOGIN", "to": "Home"}
	]
}

output = generate_flow_diagram(flow_data)

print("Flow diagram generated at:", output)
