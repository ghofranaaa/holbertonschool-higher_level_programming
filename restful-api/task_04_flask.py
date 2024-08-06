#!/usr/bin/python3
"""
This module contains a flask app.
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage for users
users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}

# Root endpoint
@app.route('/')
def home():
    return "Welcome to the Flask API!"

# Endpoint to return JSON data of all usernames
@app.route('/data')
def get_data():
    usernames = list(users.keys())
    return jsonify(usernames)

# Status endpoint
@app.route('/status')
def status():
    return "OK"

# Endpoint to return user data based on username
@app.route('/users/<username>')
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

# Endpoint to add a new user (POST request)
@app.route('/add_user', methods=['POST'])
def add_user():
    new_user = request.json
    username = new_user.get("username")
    if not username or username in users:
        return jsonify({"error": "Invalid or existing username"}), 400
    users[username] = new_user
    return jsonify({"message": "User added", "user": new_user})

if __name__ == "__main__":
    app.run(debug=True)
