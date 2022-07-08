import requests
import logging
import base64
from decouple import config
from django.http import JsonResponse    
from rest_framework.views import APIView
from rest_framework import generics, viewsets
from backend.seeding.seeder import SeedData
import rest_framework.status as REST_HTTP_STATUS
from .serializers import SeederSerializer
from django.contrib.auth.models import User

class SeedDataGenerator(APIView):
    def get_serializer(*args, **kwargs):
        return SeederSerializer(*args, **kwargs)

    def post(self, request):
        response = {}
        try:
            request_data = request.data
            app_no = request_data["no_of_apps"]
            tr_no = request_data["no_of_transactions"]
            seeder  = SeedData(app_no, tr_no)
            
            if app_no > 0:
                #This should change to the logged in user
                current_user_name = User.objects.all().first().username
                seeder.create_apps(current_user_name)
            if tr_no > 0 :
                seeder.create_transactions()
            
            status = REST_HTTP_STATUS.HTTP_200_OK
            response["message"] = f"successfull seeded  {app_no} service(s) and {tr_no} transction(s)"
            response["status"] = status
        except Exception as e:
            response["message"] = str(e)
            status = REST_HTTP_STATUS.HTTP_500_INTERNAL_SERVER_ERROR
            response["status"] = status

        return JsonResponse(response ,status=status)

class CreateOauthToken(APIView):
    pass


class CreateUser(APIView):
    def post(self, request):
        response = {}
        request_data = request.data 
        try:
            # TODO 
            # username will be auto generated as a random string
            # an ID of sorts
            user = User(username = request_data["username"],
                email= request_data["email"],
                first_name=request_data[ "first_name"],
                last_name=request_data["last_name"],
                is_active = request_data['is_active'],
                is_superuser = request_data['is_superuser'],
            )
            user.set_password(request_data["password"])
            user.save()
            response["message"] = "User successfully created"
            status_code = REST_HTTP_STATUS.HTTP_200_OK

        except Exception as e:
            response["message"] = str(e)
            status_code = REST_HTTP_STATUS.HTTP_500_INTERNAL_SERVER_ERROR

        return JsonResponse(response, status=status_code)


class GetAllUsers(generics.ListAPIView):
    def get(self, *args, **kwargs):
        response  = {}
        try:
            users = list(User.objects.values('id','username','email','first_name',
                                            'last_name','is_active',
                                            'last_login','is_staff','is_superuser',
                                            'date_joined',
                                            ))
            if len(users)>0:
                response["users"]= users
            else:
                response["message"]= "No users found"
            
            status_code = REST_HTTP_STATUS.HTTP_200_OK

        except Exception as e:
            response["message"]= str(e)
            status_code = REST_HTTP_STATUS.HTTP_500_INTERNAL_SERVER_ERROR

        return JsonResponse(response, status = status_code)


class UserViewset(viewsets.ModelViewSet):
   lookup_field = 'username' #default is id


class GetDarajaAuth(APIView):
    def get(self, request):
        api_auth = config("CONSUMER_KEY")+":"+config("CONSUMER_SECRET")
        ascii_ = api_auth.encode("utf8")
        api_auth = base64.b64encode(ascii_).decode('utf8')

        headers = {
            'Content-Type': 'ServiceApps/json',
            'Authorization': 'Basic '+ api_auth
            }
        request_params = {"grant_type":"client_credentials"}
        
        response = requests.get(config("CREDENTIALS_URL"), headers=headers, params=request_params).json()

        return JsonResponse(response)
        

