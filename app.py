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

    data = request.get_json() or {}
    message = data.get("message", "").lower().strip()

    if not message:
        reply = "🤖 कुछ लिखो, मैं सुन रहा हूँ।"

    elif any(x in message for x in ["hello", "hi", "hey", "नमस्ते"]):
        reply = "🤖 नमस्ते! मैं JAY AI हूँ। कैसे मदद करूँ? 🚀"

    elif "naam" in message or "नाम" in message:
        reply = "🤖 मेरा नाम JAY AI है। 😎"

    elif "kaise ho" in message or "कैसे हो" in message:
        reply = "🤖 मैं बिल्कुल बढ़िया हूँ! आपकी मदद के लिए तैयार हूँ। 🔥"

    elif "tum kya kar sakte" in message or "क्या कर सकते" in message:
        reply = "🤖 मैं basic coding, study और सामान्य सवालों में मदद कर सकता हूँ। 💻"

    elif "python" in message:
        reply = "🐍 Python एक आसान और powerful programming language है।"

    elif "html" in message:
        reply = "🌐 HTML website का structure बनाने के लिए इस्तेमाल होती है।"

    elif "css" in message:
        reply = "🎨 CSS website को सुंदर और stylish बनाने के लिए इस्तेमाल होती है।"

    elif "javascript" in message or "js" in message:
        reply = "⚡ JavaScript website को interactive बनाती है।"

    elif "coding" in message or "कोडिंग" in message:
        reply = "💻 Coding सीखने का सबसे अच्छा तरीका रोज practice करना है। 🚀"

    elif "website" in message or "वेबसाइट" in message:
        reply = "🌐 Website बनाने के लिए HTML, CSS और JavaScript से शुरुआत कर सकते हो।"

    elif "github" in message:
        reply = "🐙 GitHub पर तुम अपना code store और share कर सकते हो।"

    elif "termux" in message:
        reply = "📱 Termux में तुम अपने मोबाइल से coding और programming practice कर सकते हो।"

    elif "quiz" in message:
        reply = "🧠 Quiz में questions के answers देकर अपना knowledge test कर सकते हो।"

    elif "study" in message or "पढ़ाई" in message:
        reply = "📚 पढ़ाई में छोटे-छोटे goals बनाओ और regular practice करो।"

    elif "time" in message or "समय" in message:
        reply = "⏰ समय की सही planning productivity बढ़ाने में मदद करती है।"

    elif "motivation" in message or "मोटिवेशन" in message:
        reply = "🔥 धीरे-धीरे आगे बढ़ते रहो। Consistency ही असली ताकत है।"

    elif "thank" in message or "धन्यवाद" in message:
        reply = "🤖 Welcome! हमेशा मदद के लिए तैयार हूँ। ❤️"

    elif "good morning" in message:
        reply = "🌅 Good Morning! आपका दिन शानदार हो। 🚀"

    elif "good night" in message:
        reply = "🌙 Good Night! अच्छी नींद लो और कल फिर coding करेंगे। 😴"

    elif "who are you" in message or "तुम कौन" in message:
        reply = "🤖 मैं JAY AI हूँ — आपका छोटा personal assistant।"

    elif "help" in message or "मदद" in message:
        reply = "🤖 बताओ किस चीज़ में help चाहिए—Coding, Python, Website या Study?"

    elif "jay ai" in message:
        reply = "🤖 हाँ 😎 मैं JAY AI हूँ!"

    else:
        reply = (
            "🤖 तुमने कहा: " + message +
            "\n\nमैं अभी Smart Basic Mode में हूँ। 🧠"
        )

    return jsonify({"reply": reply})


app.run(
    host="0.0.0.0",
    port=int(os.environ.get("PORT", 5000))
)
