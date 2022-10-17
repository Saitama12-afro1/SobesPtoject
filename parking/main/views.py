import stat
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser


from .models import Order
from .serlializers import OrderSerializers



class IndexList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializers
    
    
class IndexDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializers

    
    