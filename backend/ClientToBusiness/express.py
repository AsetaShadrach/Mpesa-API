import base64
import logging
from datetime import datetime
from decouple import config


class MpesaExpressBackend():
    def __init__(self):
        self.pass_key = config("PASS_KEY")
        self.short_code = config("SHORT_CODE")
        self.access_token = config("ACCESS_TOKEN")
        self.account_ref = config("MPESA_EXPRESS_ACCOUNT_REF")
        self.transaction_desc = config("MPESA_EXPRESS_TRANSACTION_DESC")

    def config_request_details(self,request_data):
        try:
            self.timestamp = datetime.now().strftime(format="%Y%m%d%H%M%S")
            phone_number = request_data["phone_number"]
            amount = request_data["amount"]
            callback_url = request_data["callback_url"]
            password_parts = self.short_code+self.pass_key+self.timestamp
            ascii_pass = password_parts.encode("utf8")
            self.password = base64.b64encode(ascii_pass)

            payload = {
                "BusinessShortCode": self.short_code,
                "Password": self.password,
                "Timestamp": self.timestamp,
                "TransactionType": "CustomerPayBillOnline",
                "Amount": amount,
                "PartyA": phone_number,
                "PartyB": self.short_code,
                "PhoneNumber": phone_number,
                "CallBackURL": callback_url,
                "AccountReference": self.account_ref,
                "TransactionDesc": self.transaction_desc
            }

            return self.access_token, payload
        except Exception as e:
            logging.error(e)
            return "Not Found", None

