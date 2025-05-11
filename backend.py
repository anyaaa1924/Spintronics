from flask import Flask, request, jsonify
from twilio.rest import Client
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

# Twilio credentials
account_sid = 'YOUR_SID'
auth_token = 'YOUR_TOKEN'
twilio_phone = 'YOUR_PHNO9'
client = Client(account_sid, auth_token)


@app.route('/send-alert', methods=['POST'])
def send_alert():
    data = request.get_json()
    phone = data.get('phone')
    message = data.get('message', '🚨 Emergency Alert!')

    try:
        client.messages.create(
            body=message,
            from_=twilio_phone,
            to=phone
        )
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
