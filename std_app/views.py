from django.shortcuts import render,HttpResponse,redirect,get_object_or_404

# Create your views here.
def HomePage(request):
    return render(request,"std_app/index.html")
def AboutUS(request):
    return render(request,"std_app/about.html")
def Services(request):
    return render(request,"std_app/services.html")

