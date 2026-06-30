from flask import Flask, request, render_template_string
from google import genai
import os

app = Flask(__name__)

# Set your API key as an environment variable

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

with open("prompt.txt", "r", encoding="utf-8") as file:
    thatchprompt = file.read()

HTML = """
<!doctype html>
<html>
<head>
    <title>Thatch Bot</title>
</head>
<body>
    <h2> Thatch Bot</h2>

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

        result = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)
        response = result.text

    return render_template_string(HTML, response=response)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
