from django.shortcuts import render
from django.conf import settings
from math import pi,cos,sqrt,asin
from django.http import HttpResponse
from .models import UserData
from django.urls import reverse 
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth import authenticate,login

from rest_framework.response import Response
from rest_framework import status
from rest_framework import request
from django.shortcuts import render
from .serializer import UserDataSerializer
from rest_framework.decorators import api_view

@api_view(['POST'])
def SignupPage(request):
    if request.method == 'POST':
         data=UserDataSerializer(data=request.data)
         if data.is_valid():
             data.save()
             return Response(data.data,status=status.HTTP_201_CREATED)
           