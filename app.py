from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Experiment 6: Flask app triggered via Jenkins and GitHub Webhook"

print("Automatic Jenkins build triggered by GitHub push")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
