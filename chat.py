from flask import Flask, request, render_template_string
import google.generativeai as genai
import os

app = Flask(__name__)

# Set your API key as an environment variable
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

model = genai.GenerativeModel("gemini-1.5-flash")

with open("prompt.txt", "r", encoding="utf-8") as file:
    thatchprompt = file.read()

HTML = """
<!doctype html>
<html>
<head>
    <title>Pirate Bot</title>
</head>
<body>
    <h2>🏴 Pirate Bot</h2>

    <form method="post">
        <input name="message" style="width:300px" placeholder="Talk to Thatch">
        <button type="submit">Send</button>
    </form>

    {% if response %}
        <p><b>Thatch:</b> {{ response }}</p>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    response = ""

    if request.method == "POST":
        user_message = request.form["message"]

        prompt = f"{thatchprompt}\nUser: {user_message}"

        result = model.generate_content(prompt)
        response = result.text

    return render_template_string(HTML, response=response)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
