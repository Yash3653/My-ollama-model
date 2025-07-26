from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # Allow requests from frontend (CORS = Cross-Origin Resource Sharing)

OLLAMA_URL = "http://localhost:11434/api/generate"

@app.route('/api/ask', methods=['POST'])
def ask_model():
    data = request.get_json()
    prompt = data.get('prompt', '')

    payload = {
        "model": "llama3",  # Replace with any model you have (e.g. "mistral")
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload)
        result = response.json()
        return jsonify({"response": result.get("response", "")})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/')
def home():
    return jsonify({"message": "Flask-Ollama backend is running."})

if __name__ == '__main__':
    app.run(debug=True)
