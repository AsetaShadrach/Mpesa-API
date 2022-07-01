import requests
import logging
from decouple import config
from django.http import JsonResponse
from .serializers import (
    ServiceAppSerializer, ServiceDetailsSerializer ,
    CreateServiceSerializer 
    )                      
from .models import ServiceApp
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.views import APIView
import rest_framework.status as REST_HTTP_STATUS

class ServiceAppList(generics.ListAPIView):
    serializer_class = ServiceAppSerializer
    def get(self, *args):
        try:
            response  = {}
            queryset = ServiceApp.objects.all()
            for service in queryset:
                response[service.app_name] = {
                    "app_name" : service.app_name,
                    "active" : service.active,
                    "created_at" : service.created_at,
                    "updated_at" : service.updated_at,
                }

            status = REST_HTTP_STATUS.HTTP_200_OK

        except Exception as e:
            response["message"] = str(e)
            status = REST_HTTP_STATUS.HTTP_400_BAD_REQUEST
            
        return JsonResponse(response, status=status)


class ServiceAppDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ServiceDetailsSerializer
    def get(self,request, *args, **kwargs):
        response = {}
        try:
            app_name = kwargs["app_name"]
            service_app = ServiceApp.objects.filter(app_name = app_name).first()
            if service_app:
                response ={
                    "app_id":service_app.app_id,
                    "active" : service_app.active,
                    "tr_count_l_d" : service_app.tr_count_l_d,
                    "tr_count_l_7d" : service_app.tr_count_l_7d,
                    "tr_count_l_30d" : service_app.tr_count_l_30d,
                    "tr_cum_sum_l_d" : service_app.tr_cum_sum_l_d,
                    "tr_cum_sum_l_7d" : service_app.tr_cum_sum_l_7d,
                    "tr_cum_sum_l_30d" : service_app.tr_cum_sum_l_30d,
                    "created_at " : service_app.created_at ,
                    "updated_at" : service_app.updated_at,
                    "service_details" : service_app.service_details,
                }
                status = REST_HTTP_STATUS.HTTP_200_OK
            else:
                response = {
                    "message" : f"App with app_name: '{app_name}' was not found"
                }
                status = REST_HTTP_STATUS.HTTP_404_NOT_FOUND

        except Exception as e:
            response["message"] = str(e)
            status = REST_HTTP_STATUS.HTTP_400_BAD_REQUEST
            response["status"] = status
        
        return JsonResponse(response, status=status)


class UpdateServiceDetails(APIView):
    def put(self, request):
        response = {}
        change_description = ''
        try:
            request_data = request.data
            app_name = request_data["app_name"]
            service = ServiceApp.objects.filter(app_name=app_name).first()
            
            if request_data.get("app_name"):
                new_app_name = request_data.get("app_name")
                service.update(app_name = new_app_name)
                message = f"Changed app_name of {app_name} to {new_app_name}. "
                change_description = change_description + message

            if request_data.get("active"): 
                active = request_data.get("active")
                service.update(active = active)
                message = f"Changed app active status of {app_name} to {str(active)}. "
                change_description = change_description + message
            
            logging.info(change_description)

            response["message"] = change_description
            status = REST_HTTP_STATUS.HTTP_200_OK

        except Exception as e:
            response["message"] = str(e)
            status = REST_HTTP_STATUS.HTTP_400_BAD_REQUEST
            response["status"] = status

        return JsonResponse(response, status=status)
    

class CreateService(generics.CreateAPIView):
    def get_serializer(self, *args, **kwargs):
        return CreateServiceSerializer(*args, **kwargs)
        _
    def post(self, request):
        response = {}
        try:
            request_data = request.data
            # Use the username/email of the user in session as the creator
            user  = User.objects.all().first()
            app = ServiceApp(creator = user.username ,
                        app_name = request_data.get("app_name"),
                        active = request_data.get("active"))                        
            app.save()
        
            response_code = REST_HTTP_STATUS.HTTP_201_CREATED
            status_code = REST_HTTP_STATUS.HTTP_200_OK
            response["message"] = f"Successfully created service  {app.app_name} "
            response["response_code"] = response_code 
            return JsonResponse(response, status = status_code)

        except Exception as e:
            response_code = REST_HTTP_STATUS.HTTP_500_INTERNAL_SERVER_ERROR
            status_code = REST_HTTP_STATUS.HTTP_500_INTERNAL_SERVER_ERROR
            response["message"]= str(e)
            response["response_code"] = response_code
            return JsonResponse(response, status = status_code)
            