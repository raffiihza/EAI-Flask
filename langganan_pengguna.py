from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/user")
def get_user():
    user = {"name": "John", "age": 30}
    return jsonify(user)

if __name__ == "__main__":
    app.run(port=5000)