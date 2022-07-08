from .models import Transaction
from rest_framework import serializers

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['transaction_id','app_id','transaction_type','status','response_code','created_at','updated_at']

class SendMoneySerializer(serializers.Serializer):
    number  = serializers.IntegerField()
    amount  = serializers.IntegerField(max_value=150000)
    callback_url = serializers.CharField()