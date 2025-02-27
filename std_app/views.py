from django.shortcuts import render,HttpResponse,redirect,get_object_or_404

# Create your views here.
def HomePage(request):
    return render(request,"std_app/index.html")