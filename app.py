from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    try:
        response = requests.get("https://zenquotes.io/api/random")
        data = response.json()[0]
        quote = data["q"]
        author = data["a"]
    except Exception as e:
        quote = "Could not fetch quote."
        author = str(e)
    return render_template("index.html", quote=quote, author=author)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
