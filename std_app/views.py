from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .models import Student
# Create your views here.
def HomePage(request):
    users = Student.objects.all()
    context={
        'users':users
    }
    return render(request,"std_app/index.html",context)

def AboutUS(request):
    return render(request,"std_app/about.html")

def Services(request):
    return render(request,"std_app/services.html")

def Add_Std(request):
    if request.method == "POST":
        name = request.POST.get("name")
        roll = request.POST.get("roll")
        dept = request.POST.get("dept")
        address = request.POST.get("address")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        
        if name and roll and dept and address and phone and email :
            user = Student(name=name,roll=roll,dept=dept,address=address,phone=phone,email=email)
            user.save()
            return redirect("home")
    
    return render(request,"std_app/add_std.html")

def EditStd(request, id):
    user = get_object_or_404(Student, id=id)

    if request.method == "POST":
        user.name = request.POST.get("name")
        user.roll = request.POST.get("roll")
        user.dept = request.POST.get("dept")
        user.address = request.POST.get("address")
        user.phone = request.POST.get("phone")
        user.email = request.POST.get("email")
        user.save()
        return redirect("home")  # Redirect to home after updating

    return render(request, "std_app/update.html", {"user": user})


def DeleteStd(request, id):
    if request.method == "POST":
        user = get_object_or_404(Student, id=id)
        user.delete()
        return redirect('home')  # Redirect back to home after deletion

    return redirect('home')