from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return send_from_directory(".", "ai.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    message = data.get("message", "").lower().strip()

    if "hello" in message or "hi" in message:
        reply = "🤖 Hello! Main JAY AI hoon. Kaise ho?"
    elif "naam" in message:
        reply = "🤖 Mera naam JAY AI hai."
    elif "kaise ho" in message:
        reply = "🤖 Main bilkul ready hoon! 🚀"
    elif "jay ai" in message:
        reply = "🤖 Haan! Main JAY AI hoon 😎"
    elif "help" in message:
        reply = "🤖 Main tumhari help karne ke liye ready hoon."
    else:
        reply = "🤖 Tumne kaha: " + message

    return jsonify({"reply": reply})

app.run(
    host="0.0.0.0",
    port=int(os.environ.get("PORT", 5000))
)
