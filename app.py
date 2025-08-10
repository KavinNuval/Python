from flask import Flask, request, jsonify

app = Flask(__name__)
users = {}

@app.route("/users", methods=["GET"])
def get_all_users():
    return jsonify(users)

@app.route("/users/<int:user_id>", methods=["GET"])
def get_single_user(user_id):
    if user_id in users:
        return jsonify({user_id: users[user_id]})
    else:
        return jsonify({"message": "User not found"}), 404

@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    if not data or "name" not in data or "email" not in data:
        return jsonify({"message": "Please provide name and email"}), 400
    new_id = len(users) + 1
    users[new_id] = {"name": data["name"], "email": data["email"]}
    return jsonify({"message": "User created", "id": new_id}), 201

@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    if user_id not in users:
        return jsonify({"message": "User not found"}), 404
    data = request.get_json()
    users[user_id].update(data)
    return jsonify({"message": "User updated"})

@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    if user_id in users:
        del users[user_id]
        return jsonify({"message": "User deleted"})
    else:
        return jsonify({"message": "User not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
