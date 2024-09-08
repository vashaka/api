from flask import Flask, request, jsonify

app = Flask(__name__)

data = {"message": "Hello, World!"}

@app.route('/get-data', methods=['GET'])
def get_data():
    return jsonify(data), 200

@app.route('/post-data', methods=['POST'])
def post_data():
    posted_data = request.get_json()

    return jsonify({"message": "Data received successfully!", "data": posted_data}), 201

if __name__ == '__main__':
    app.run(debug=True)
