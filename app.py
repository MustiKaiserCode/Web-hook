from flask import Flask, request, jsonify

app = Flask(__name__)

# Define your verification token (must be between 32-80 characters)
VERIFICATION_TOKEN = "ebay-verification-token-1234567890abcdef1234"

@app.route('/ebay-notifications', methods=['GET', 'POST'])
def ebay_notifications():
    # Check for the verification token in the headers
    token = request.headers.get('X-Ebay-Verification-Token')
    
    # If the token is missing or incorrect, return an error
    if token != VERIFICATION_TOKEN:
        return jsonify({"error": "Unauthorized"}), 401

    # Handle GET request (e.g., verification)
    if request.method == 'GET':
        return jsonify({"message": "GET request received"}), 200

    # Handle POST request (e.g., process notification)
    elif request.method == 'POST':
        data = request.json
        print("Received POST data:", data)
        return jsonify({"message": "POST request received"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
