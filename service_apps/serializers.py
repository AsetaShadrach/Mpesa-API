from .models import ServiceApps
from rest_framework import serializers

class ServiceAppsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceApps
        fields = ('app_id','creator','active','created_at','updated_at','change_description')

