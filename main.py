
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Hello, CI/CD with GCP and Flask!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)