import requests
import logging
from decouple import config
from django.http import JsonResponse    
from rest_framework.views import APIView
from rest_framework import generics
from backend.seeding.seeder import SeedData
import rest_framework.status as REST_HTTP_STATUS

class Generator(APIView):
    def post(self, request):
        response = {}
        try:
            request_data = request.data
            app_no = request_data["no_of_apps"]
            tr_no = request_data["no_of_transactions"]
            seeder  = SeedData(app_no, tr_no)

            if app_no > 0:
                seeder.create_apps()
            if tr_no > 0 :
                seeder.create_transactions()
            
            status = REST_HTTP_STATUS.HTTP_200_OK
            response["message"] = f"successfull seeded  {app_no} service(s) and {tr_no} transction(s)"
            response["status"] = status
        except Exception as e:
            response["message"] = str(e)
            status = REST_HTTP_STATUS.HTTP_400_BAD_REQUEST
            response["status"] = status

        return JsonResponse(response ,status=status)

class CreateOauthToken(APIView):
    pass
