from src import app
from flask import jsonify


@app.route("/")
def home():
    return "Hasura Hello from github"

# Uncomment to add a new URL at /new

@app.route("/json")
def json_message():
    return jsonify(message="Hello World")
