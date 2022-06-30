from rest_framework import serializers

class SeederSerializer(serializers.Serializer):
    no_of_apps = serializers.IntegerField()
    no_of_transactions = serializers.IntegerField()

