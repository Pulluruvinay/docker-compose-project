from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow requests from frontend container

@app.route("/api/message")
def message():
    return jsonify({"message": "Welcome the docker's world.. 🚀"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
