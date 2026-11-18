
from flask import Flask, jsonify
import os

app = Flask(__name__)

APP_VERSION = os.getenv("APP_VERSION", "1.0.0")

@app.route("/")
def home():
    return jsonify({
        "application": "production-webapp",
        "version": APP_VERSION,
        "status": "running",
        "message": "Hello from Kubernetes!"
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

@app.route("/version")
def version():
    return jsonify({"version": APP_VERSION})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)