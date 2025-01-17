from rest_framework import serializers
from .models import UserData

class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = '__all__'
