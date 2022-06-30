from .models import ServiceApp
from rest_framework import serializers

class ServiceAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceApp
        fields = ('app_id','creator','active','created_at','updated_at')

class ServiceDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceApp
        fields = ["app_id", "creator", "active",  "tr_count_l_d",  "tr_count_l_7d",
                "tr_count_l_30d",  "tr_cum_sum_l_d",  "tr_cum_sum_l_7d",
                "tr_cum_sum_l_30d",  "created_at",  "updated_at",
                "service_details"]

class CreateServiceSerializer(serializers.Serializer):
    app_name = serializers.CharField()
    active = serializers.BooleanField()