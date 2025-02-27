from django.contrib import admin
from django.urls import path
from std_app import views

urlpatterns = [
    path("",views.HomePage,name='home'),
    path("about/",views.AboutUS,name='about'),
    path("services/",views.Services,name='services'),
]