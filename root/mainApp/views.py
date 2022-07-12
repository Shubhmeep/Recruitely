from re import L
from django.http import HttpResponse
from django.shortcuts import render
from numpy import number
from mainApp.models import project as pp
project_list = [
    {'id':'1',
    'title':"Ecommerce Website",
    'description':'Fully functional ecommerce website'},
    { 'id':'2',
    'title':"Portfolio Website",
    'description':'This wasaproject whereIbuilt out my portfolio'},
    {'id':'3',
    'title':"Social Network",
    'description':'Awesome open source projectIam still working on'}
]
    
   
    
# Create your views here.
def projects(request):
    projectlist = pp.objects.all()
    context = {'projectlist':projectlist}
    return render(request,'mainApp/projects.html',context)

def mainpage(request):
    return render(request,'main.html')

def project(request,pk):
    projectlist = pp.objects.get(id=pk)
   
    return render(request,'mainApp/single-project.html',{'project':projectlist})