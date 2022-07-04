from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def projects(request):
    return render(request,'mainApp/projects.html')

def mainpage(request):
    return render(request,'main.html')

def project(request,pk):
    return render(request,'mainApp/single-project.html')