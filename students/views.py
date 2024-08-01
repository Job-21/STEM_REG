from django.shortcuts import render, redirect
from .models import StudentsData
import requests
# Created my views here.

def index(request):
    api_data = requests.get("http://localhost:8000/students/data/all").json()
    print(type(api_data))
    data = StudentsData.objects.all().values()
    
    context = {
        "data":data
    }
    return render(request, "index.html", api_data )

def register(request):
    if request.method == "POST":
        firstName = request.POST.get("fname")
        LastName = request.POST.get("lname")
        course = request.POST.get("course")
        year = request.POST.get("year")

        my_student = StudentsData(fname=firstName, lname=LastName, course=course, year=year)
        my_student.save()
        return redirect("index")
    return render(request, "register.html")
