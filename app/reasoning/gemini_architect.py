import os
import google.generativeai as genai



genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


USE_REAL_GEMINI = True

def generate_architecture(flow_data):
	prompt = f"""
You are a senior software architect.

Given the following inferred UI flow:
{flow_data}

1. Recommend frontend framework (web or mobile).
2. Recommend backend stack (if needed).
3. Suggest authentication mechanism.
4. Generate a clean project folder structure.
5. Explain briefly why this architecture fits the UI.
"""

	# Try real Gemini
	if USE_REAL_GEMINI:
		try:
			client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
			response = client.models.generate_content(
				model="gemini-2.0-flash",
				contents=prompt
			)
			return response.text
		except Exception as e:
			print("⚠️ Gemini API failed, using fallback reasoner.")
			print("Reason:", e)

	# Fallback (local reasoning)
	return f"""
	
Recommended Frontend:
- React (Vite)

Backend:
- Node.js + Express

Authentication:
- JWT-based authentication

Project Structure:
frontend/
 ├── src/
 │   ├── pages/
 │   │   ├── Login.jsx
 │   │   ├── Signup.jsx
 │   │   └── Home.jsx
 │   ├── components/
 │   ├── services/
 │   └── App.jsx
backend/
 ├── controllers/
 ├── routes/
 ├── models/
 └── server.js

Reasoning:
This architecture fits a login/signup flow with simple navigation and authentication.
"""
