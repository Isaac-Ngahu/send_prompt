import requests
from flask import json, jsonify
from main import insert_token

def send_payment_request(number,amount):
    try:
        insert_token()
        get_url = "https://payment-tracker.onrender.com/get_access_token"
        response = requests.get(url=get_url)
        token = response.json().get("accessToken")
        url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        data = {
    "BusinessShortCode": 174379,
    "Password": "MTc0Mzc5YmZiMjc5ZjlhYTliZGJjZjE1OGU5N2RkNzFhNDY3Y2QyZTBjODkzMDU5YjEwZjc4ZTZiNzJhZGExZWQyYzkxOTIwMjQwNjIxMTEzNDMx",
    "Timestamp": "20240621113431",
    "TransactionType": "CustomerPayBillOnline",
    "Amount": amount,
    "PartyA": number,
    "PartyB": 174379,
    "PhoneNumber": number,
    "CallBackURL": "https://payment-tracker.onrender.com/record_response",
    "AccountReference": "Spares",
    "TransactionDesc": "Payment of spare"
  }
        session = requests.session()
        session.headers.update({'Content-Type': 'application/json',
                                'Authorization': f'Bearer {token}'})
        response = session.post(url, json=data)
        print(response.json())
        return response
    except Exception as e:
        print(str(e))


# send_payment_request()
