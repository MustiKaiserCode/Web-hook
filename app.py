import sys
from flask import Flask, request, jsonify

app = Flask(__name__)

# Define your verification token
VERIFICATION_TOKEN = "ebay-verification-token-1234567890abcdef1234"

@app.route('/ebay-notifications', methods=['GET', 'POST'])
def ebay_notifications():
    # Check for the verification token in the headers
    token = request.headers.get('X-Ebay-Verification-Token')
    print("Received token:", token)
    sys.stdout.flush()  # Force the log to be written immediately

    # If the token is missing or incorrect, return an error
    if token != VERIFICATION_TOKEN:
        return jsonify({"error": "Unauthorized"}), 401

    # Handle GET request (e.g., webhook verification)
    if request.method == 'GET':
        # Extract the challenge_code from the query parameters
        challenge_code = request.args.get('challenge_code')
        if not challenge_code:
            return jsonify({"error": "Missing challenge_code"}), 400
        
        # Return the challenge_code to complete verification
        return jsonify({"challengeResponse": challenge_code}), 200

    # Handle POST request (e.g., process notification)
    elif request.method == 'POST':
        data = request.json
        print("Received POST data:", data)
        sys.stdout.flush()  # Force the log to be written immediately
        return jsonify({"message": "POST request received"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
