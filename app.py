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

    if not message:
        reply = "🤖 कुछ लिखो, मैं सुन रहा हूँ।"

    elif "hello" in message or "hi" in message or "नमस्ते" in message:
        reply = "🤖 नमस्ते! मैं JAY AI हूँ। कैसे मदद करूँ? 🚀"

    elif "naam" in message or "नाम" in message:
        reply = "🤖 मेरा नाम JAY AI है। 😎"

    elif "kaise ho" in message or "कैसे हो" in message:
        reply = "🤖 मैं बिल्कुल बढ़िया हूँ और आपकी मदद के लिए तैयार हूँ! 🔥"

    elif "python" in message:
        reply = "🐍 Python एक आसान और powerful programming language है।"

    elif "html" in message:
        reply = "🌐 HTML website का structure बनाने के लिए इस्तेमाल होती है।"

    elif "css" in message:
        reply = "🎨 CSS website को सुंदर और stylish बनाने के लिए इस्तेमाल होती है।"

    elif "javascript" in message or "js" in message:
        reply = "⚡ JavaScript website को interactive बनाती है।"

    elif "coding" in message or "कोडिंग" in message:
        reply = "💻 Coding सीखने के लिए रोज थोड़ा practice करो। तुम अच्छा कर रहे हो! 🚀"

    elif "help" in message or "मदद" in message:
        reply = "🤖 मैं Python, HTML, CSS और JavaScript की basic जानकारी में मदद कर सकता हूँ।"

    elif "jay ai" in message:
        reply = "🤖 हाँ 😎 मैं JAY AI हूँ!"

    else:
        reply = "🤖 समझ गया: " + message + "\n\nमैं अभी Smart Basic Mode में हूँ। 🧠"


    return jsonify({"reply": reply})


app.run(
    host="0.0.0.0",
    port=int(os.environ.get("PORT", 5000))
)
