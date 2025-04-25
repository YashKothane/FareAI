from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
from .models import Placeinfo
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import request, status
from math import cos, asin, sqrt, pi
from django.template import loader
from django.urls import reverse
# from rest_framework.simplejwt.authentication import JWTAuthentication

# class wishlist(APIVIEW):
#     permission_classes=[IsAuthenticated]
#     authentication_classes=[JWTAuthentication]

def logic(sa,da):
      place1= Placeinfo.objects.get(place=sa)
      sa_lat=place1.latitude
      sa_long=place1.longitude
      place2= Placeinfo.objects.get(place=da)
      da_lat=place2.latitude
      da_long=place2.longitude
      final_distance= distance(sa_lat, sa_long, da_lat,da_long)
      return final_distance
def distance(lat1, lon1, lat2, lon2):
    r = 6371 # km
    p = pi / 180

    a = 0.5 - cos((lat2-lat1)*p)/2 + cos(lat1*p) * cos(lat2*p) * (1-cos((lon2-lon1)*p))/2
    return 2 * r * asin(sqrt(a))

def comapare(request):
    if request.method =='POST':   
      final_distance = None
      city2 =request.POST.get("CITY")
      sa =request.POST.get("SA")
      da=request.POST.get("DA")
      final_distance=logic(sa,da)
      return redirect(f"{reverse('result')}?final_distance={final_distance}")
   
         
    return render(request, 'compare.html')

def result(request):
    final_distance = request.GET.get('final_distance', None)
    return render(request, 'result.html', {'final_distance': final_distance})

def our(final_distance):
  
    ola=(final_distance*10)+30