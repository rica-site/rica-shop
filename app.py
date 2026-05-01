from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import base64
from datetime import datetime

app = Flask(__name__)
CORS(app)

consumer_key = "YOUR_KEY"
consumer_secret = "YOUR_SECRET"
shortcode = "174379"
passkey = "YOUR_PASSKEY"

def get_access_token():
    url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
    res = requests.get(url, auth=(consumer_key, consumer_secret))
    return res.json()['access_token']

@app.route('/pay', methods=['POST'])
def pay():
    data = request.json
    phone = data['phone']
    amount = data['amount']

    access_token = get_access_token()

    url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"

    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    password = base64.b64encode((shortcode + passkey + timestamp).encode()).decode()

    headers = {"Authorization": f"Bearer {access_token}"}

    payload = {
        "BusinessShortCode": shortcode,
        "Password": password,
        "Timestamp": timestamp,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": amount,
        "PartyA": phone,
        "PartyB": shortcode,
        "PhoneNumber": phone,
        "CallBackURL": "https://example.com/callback",
        "AccountReference": "RICA",
        "TransactionDesc": "Payment"
    }

    response = requests.post(url, json=payload, headers=headers)
    return jsonify(response.json())

app.run(debug=True)
