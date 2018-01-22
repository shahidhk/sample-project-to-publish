from src import app
from flask import jsonify


@app.route("/")
def home():
    return "Hello World - Hasura was here at #Code4Beer! and hacked"

# Uncomment to add a new URL at /new

@app.route("/json")
def json_message():
    return jsonify(message="Hello json")
