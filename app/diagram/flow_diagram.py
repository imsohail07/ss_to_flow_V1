from graphviz import Digraph

def generate_flow_diagram(flow_data, output_path="diagrams/user_flow"):
	dot = Digraph(comment="User Flow Diagram", format="png")

	# Add nodes
	dot.node(flow_data["screen_name"], flow_data["screen_name"])

	for action in flow_data["actions"]:
		dot.node(action["to"], action["to"])
		dot.edge(
			action["from"],
			action["to"],
			label=action["action"]
		)

	# Save diagram
	dot.render(output_path, cleanup=True)
	return output_path
