from django.urls import path,include
from django.contrib import admin
from .import views
from .views import SignupPage

urlpatterns = [
# path('', views.HomePage, name='home'),
path('usersignup/',views.SignupPage,name="login"),
]