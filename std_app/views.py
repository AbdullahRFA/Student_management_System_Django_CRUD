from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Student

# Home Page
def HomePage(request):
    users = Student.objects.all()
    context = {'users': users}
    return render(request, "std_app/index.html", context)

# About Page
def AboutUS(request):
    return render(request, "std_app/about.html")

# Services Page
def Services(request):
    return render(request, "std_app/services.html")

# Add New Student
def Add_Std(request):
    if request.method == "POST":
        name = request.POST.get("name")
        roll = request.POST.get("roll")
        dept = request.POST.get("dept")
        address = request.POST.get("address")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        
        if name and roll and dept and address and phone and email:
            user = Student(name=name, roll=roll, dept=dept, address=address, phone=phone, email=email)
            user.save()
            messages.success(request, "Student added successfully! 🎉")
            return redirect("home")
        else:
            messages.error(request, "All fields are required! ❌")

    return render(request, "std_app/add_std.html")

# Edit Student Details
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
        messages.success(request, "Student details updated successfully! ✅")
        return redirect("home")

    return render(request, "std_app/update.html", {"user": user})

# Delete Student
def DeleteStd(request, id):
    if request.method == "POST":
        user = get_object_or_404(Student, id=id)
        user.delete()
        messages.success(request, "Student deleted successfully! 🗑️")
        return redirect('home')

    messages.error(request, "Something went wrong! ❌")
    return redirect('home')