from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/product")
def get_product():
    product = {"name": "Laptop", "price": 1000}
    return jsonify(product)

if __name__ == "__main__":
    app.run(port=5001)