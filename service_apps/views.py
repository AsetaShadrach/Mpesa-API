import requests
import logging
from decouple import config
from django.http import JsonResponse
from .serializers import ServiceAppsSerializer                          
from .models import ServiceApps
from rest_framework import generics 


class ServiceAppsList(generics.ListAPIView):
    serializer_class = ServiceAppsSerializer
    def get():
        queryset = ServiceApps.objects.all()
        return queryset

class ServiceAppsDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ServiceAppsSerializer
    def get(app_id):
        service_app = ServiceApps.objects.filter(app_id = app_id).first()
        return service_app
