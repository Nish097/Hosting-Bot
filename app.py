from flask import Flask, request
from bot import run_show  # This calls your main hosting script

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "✅ AI Bot is alive and ready!"

@app.route("/start", methods=["POST"])
def start_show():
    try:
        run_show()
        return "🎤 Show has started successfully!"
    except Exception as e:
        return f"❌ Error: {e}"

if __name__ == "__main__":
    app.run(debug=True)
