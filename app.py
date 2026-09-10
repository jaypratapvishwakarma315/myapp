from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    message = data.get("message", "")

    reply = "🤖 JAY AI: Tumne kaha — " + message

    return jsonify({"reply": reply})

import os
app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
