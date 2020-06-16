# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets
from .serializers import HotelSerializer
from .models import Hotel

# Create your views here.
class HotelsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

