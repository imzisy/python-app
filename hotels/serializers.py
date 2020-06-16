from rest_framework import serializers
from .models import Hotel
from django.conf import settings

class HotelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hotel
        fields = '__all__'