from flask import Flask, request, jsonify
import hashlib

app = Flask(__name__)

# Define your verification token
VERIFICATION_TOKEN = "ebay-verification-token-1234567890abcdef1234"

# Add a route for the root URL
@app.route('/')
def home():
    return "Webhook endpoint is running!", 200

@app.route('/ebay-notifications', methods=['GET', 'POST'])
def ebay_notifications():
    # Check for the verification token in the headers
    token = request.headers.get('X-Ebay-Verification-Token')
    print("Received token:", token)

    # If the token is missing or incorrect, return an error
    if token != VERIFICATION_TOKEN:
        return jsonify({"error": "Unauthorized"}), 401

    # Handle GET request (e.g., webhook verification)
    if request.method == 'GET':
        # Extract the challenge_code from the query parameters
        challenge_code = request.args.get('challenge_code')
        if not challenge_code:
            return jsonify({"error": "Missing challenge_code"}), 400

        # Define the endpoint URL (must match the URL provided to eBay)
        endpoint = "https://web-hook-1o1x.onrender.com/ebay-notifications"

        # Hash the challenge_code, verification token, and endpoint URL
        hash_input = challenge_code + VERIFICATION_TOKEN + endpoint
        challenge_response = hashlib.sha256(hash_input.encode()).hexdigest()

        # Return the challengeResponse in JSON format
        return jsonify({"challengeResponse": challenge_response}), 200

    # Handle POST request (e.g., process notification)
    elif request.method == 'POST':
        data = request.json
        print("Received POST data:", data)
        return jsonify({"message": "POST request received"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
