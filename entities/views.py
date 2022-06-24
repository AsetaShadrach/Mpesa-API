import requests
import logging
from decouple import config
from django.http import JsonResponse
from .serializers import (  ServiceAppsSerializer, 
                            TransactionSerializer,
                            SendMoneySerializer
                        )
from .models import ServiceApps, Transaction
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
import rest_framework.status as REST_HTTP_STATUS
from backend.ClientToBusiness.express import MpesaExpressBackend
from backend.logging.log_config import make_logger


class ServiceAppssList(generics.ListAPIView):
    queryset = ServiceApps.objects.all()
    serializer_class = ServiceAppsSerializer
    

class TransactionsList(generics.ListAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class ServiceAppsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ServiceApps.objects.all()
    serializer_class = ServiceAppsSerializer


class TransactionDetail(generics.RetrieveUpdateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class MpesaCallbackUrl(APIView):
    def post(self, request):
        return JsonResponse(request.data)


class MpesaExpress(GenericAPIView, APIView):
    serializer_class = SendMoneySerializer
    def post(self, request):
        try:
            express_url = config("EXPRESS_URL")
            express_req = MpesaExpressBackend()
            request_data = request.data
            access_token, payload = express_req.config_request_details(request_data)
            
            bearer_token = 'Bearer ' + access_token

            headers = {
            'Content-Type': 'ServiceApps/json',
            'Authorization': bearer_token
            }

            response = requests.post(express_url, headers=headers, json= payload)
            logging.info(response.text)
            
            return JsonResponse({"status":response.status_code} , 
                    status=REST_HTTP_STATUS.HTTP_200_OK)
        except Exception as e:
            print(str(e))
            return JsonResponse({"status":response.status_code} , 
                    status=REST_HTTP_STATUS.HTTP_200_OK)


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
