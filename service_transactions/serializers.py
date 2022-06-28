from .models import Transaction
from rest_framework import serializers

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('transaction_id','app_id','status','response_code','created_at','updated_at')

class SendMoneySerializer(serializers.Serializer):
    number  = serializers.IntegerField()
    amount  = serializers.DecimalField(max_digits=6, decimal_places=2, max_value=150000)
    callback_url = serializers.CharField()