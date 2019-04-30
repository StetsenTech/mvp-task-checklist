from flask import Flask, jsonify
from requests import Response

app = Flask(__name__)

@app.route("/")
def checklist():
    message = {
        "message": "success"
    }

    return jsonify(message), 200

