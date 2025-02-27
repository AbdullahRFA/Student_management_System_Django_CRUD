from django.contrib import admin
from django.urls import path
from std_app import views

urlpatterns = [
    path("",views.HomePage,name='home'),
]