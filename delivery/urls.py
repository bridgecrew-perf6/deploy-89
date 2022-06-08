from django.http import JsonResponse
from django.urls import path
from delivery import views
from rest_framework import serializers
from rest_framework.parsers import JSONParser 

urlpatterns = [
   path('orders/', views.order_list, name="order_list")
]
