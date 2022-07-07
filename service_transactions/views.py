from urllib import response
import requests
import logging
from decouple import config
import uuid
from django.http import JsonResponse
from .serializers import (
                            TransactionSerializer,
                            SendMoneySerializer
                        )
from .models import Transaction
from service_apps.models import ServiceApp
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
import rest_framework.status as REST_HTTP_STATUS
from backend.processing.transaction_processing import (
    CreateTransaction, MpesaExpressBackend,
    CallbackProcessing
)

from backend.logging.log_config import make_logger
from oauth2_provider.contrib.rest_framework import (
    TokenHasReadWriteScope
)


class TransactionsList(generics.ListAPIView):
    queryset = Transaction.objects.values()
    serializer_class = TransactionSerializer
    def get(self, request, *args, **kwargs):
        response = {}
        # apparently serializer.data is a bit slower than just using something like .values()
        # therefore opted for get queryset
        response["transactions"] = list(self.get_queryset())
        status = REST_HTTP_STATUS.HTTP_200_OK
        return JsonResponse(response, status=status)


class TransactionDetail(generics.RetrieveUpdateAPIView):
    serializer_class = TransactionSerializer
    def get(self, request, *args, **kwargs):
        response = {}
        transaction_id =  kwargs.get("transaction_id")
        try:
            tr = get_object_or_404(Transaction, transaction_id=transaction_id)
            response = self.serializer_class(tr).data
            status = REST_HTTP_STATUS.HTTP_200_OK
            return JsonResponse(response, status=status)
        except Exception as e:
            response["message"] = str(e)
            status = REST_HTTP_STATUS.HTTP_400_BAD_REQUEST
            return JsonResponse(response, status=status)


class FilterTansactions(generics.ListAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    def post(self,request, *args, **kwargs):
        response = {}
        request_data = request.data
        transaction_id = request_data.get("transaction_id")
        transaction_code = request_data.get("transaction_code")
        app_id = request_data.get("app_id")
        transaction_type = str(request_data.get("transaction_type")).upper()
        status = request_data.get("status")
        response_code = request_data.get("response_code")
        created_at_start = request_data.get("created_at_start")
        created_at_end = request_data.get("created_at_end")
        updated_at_start = request_data.get("updated_at_start")
        updated_at_end = request_data.get("updated_at_end")
        
        try:
            if transaction_id:
                self.queryset = self.queryset.filter(transaction_id=transaction_id)
            if transaction_code:
                self.queryset = self.queryset.filter(transaction_code=transaction_code)
            if app_id:
                self.queryset = self.queryset.filter(app_id=app_id)
            if transaction_type:
                self.queryset = self.queryset.filter(transaction_type=transaction_type)
            if status:    
                self.queryset = self.queryset.filter(status=status)
            if response_code:
                self.queryset = self.queryset.filter(response_code =response_code)
            if created_at_end and created_at_start:
                self.queryset = self.queryset.filter(created_at__gte=created_at_start,
                    created_at__lte = created_at_end)
            if updated_at_end and updated_at_start:
                self.queryset = self.queryset.filter(updated_at__gte=updated_at_start,
                    updated_at__lte=updated_at_end)

            response["transactions"] = list(self.queryset.values())
            status = REST_HTTP_STATUS.HTTP_200_OK
            return JsonResponse(response,status=status)

        except Exception as e:
            response["message"] = str(e)
            status = REST_HTTP_STATUS.HTTP_400_BAD_REQUEST
            return JsonResponse(response, status=status)


class MpesaCallbackUrl(APIView):
    def post(self, request):
        print(request.data)
        return JsonResponse(request.data)


class MpesaExpress(GenericAPIView, APIView):
    #permission_classes = [  permissions.IsAuthenticated,
     #                       TokenHasReadWriteScope
      #                  ]
    serializer_class = SendMoneySerializer
    def post(self, request):
        response  = {}
        mpesa_request = {}
        request_data = request.data
        try:
            express_url = config("EXPRESS_URL")
            express_req = MpesaExpressBackend()
            mpesa_request["phone_number"] = request_data["phone_number"]
            mpesa_request["amount"] = request_data["amount"]
            mpesa_request["callback_url"] = request_data["callback_url"]

            cr_tr  = CreateTransaction()
            result = cr_tr.save_transaction_init(
                request_data["app_id"],
                request_data["transaction_code"],
                str(request_data["transaction_type"]).upper()
            )

            access_token, payload = express_req.config_request_details(mpesa_request)            
            bearer_token = 'Bearer ' + access_token
            headers = {
            'Content-Type': 'ServiceApps/json',
            'Authorization': bearer_token
            }
            mpesa_response = requests.post(express_url, headers=headers, json= payload).json()

            response_message = mpesa_response["errorMessage"]
            response_code = mpesa_response["errorCode"]
            status = REST_HTTP_STATUS.HTTP_200_OK

            response["transaction_code"] = request_data["transaction_code"]
            response["service_transaction_id"] = cr_tr.transaction.transaction_id
            response["mpesa_response"] = mpesa_response
            result = cr_tr.save_transaction_final(status , response_code, response_message)

            logging.info(mpesa_response) 

            return JsonResponse(response, status=status)
        except Exception as e:
            logging.error(e)
            response["message"]=str(e)
            return JsonResponse(response, status=REST_HTTP_STATUS.HTTP_500_INTERNAL_SERVER_ERROR)


class SendMoney(APIView):
    """
    name : (str)
    number : (str)
    """
    def post(self, request):
        data = JSONParser().parse(request)
        print(data)


class ReverseSendMoney(APIView):
    """
    name : (str)
    number : (str)
    """
    def post(self, request):
        data = JSONParser().parse(request)
        print(data)
