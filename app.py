from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/ebay-notifications', methods=['GET', 'POST'])
def ebay_notifications():
    if request.method == 'GET':
        # Handle GET request (e.g., verification)
        return jsonify({"message": "GET request received"}), 200
    elif request.method == 'POST':
        # Handle POST request (e.g., process notification)
        data = request.json
        print("Received POST data:", data)
        return jsonify({"message": "POST request received"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)