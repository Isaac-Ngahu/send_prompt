from flask_cors import CORS
from flask import Flask,request
from test import send_payment_request
app = Flask(__name__)
CORS(app)
@app.route("/send_prompt",methods=['POST'])
def send_payment_prompt():
    try:
        data = request.get_json()
        number = data["phoneNumber"]
        amount = data["amount"]
        response=send_payment_request(number,amount)
        print(response)
        return "sent",200
    except Exception as e:
        print(str(e))




app.run(host="0.0.0.0",debug=False)