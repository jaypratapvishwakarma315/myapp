from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    message = data.get("message", "")

    reply = "🤖 JAY AI: Tumne kaha — " + message

    return jsonify({"reply": reply})

app.run(host="0.0.0.0", port=5000)

