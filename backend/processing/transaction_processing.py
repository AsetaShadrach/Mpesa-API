import uuid
import base64
import logging
from datetime import datetime
from decouple import config
from service_transactions.models import Transaction
from service_apps.models import ServiceApp
from django.shortcuts import get_object_or_404


class CreateTransaction():
    def __init__(self):
        self.transaction = Transaction()

    def save_transaction_init(self, app_id, transaction_code,
                                transaction_type):
        self.transaction.transaction_id = uuid.uuid4()
        self.transaction.app_id = get_object_or_404(ServiceApp, app_id=app_id)
        self.transaction.transaction_type = Transaction.TransactionType[transaction_type]
        self.transaction.transaction_code = transaction_code
        self.transaction.status = Transaction.TransactionStatus.PENDING_EXTERNAL
        self.transaction.response_code = 200
        self.transaction.save()
        return 0
    
    def save_transaction_final(self, status_code, response_code, response_message):
        self.transaction.status = Transaction.TransactionStatus.SUCCESSFUL
        self.transaction.response_code = response_code
        self.transaction.status_code = status_code
        self.transaction.response_message = response_message
        self.transaction.save()
        return 0


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


class CallbackProcessing():
    pass