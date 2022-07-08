from re import L
from django.http import HttpResponse
from django.shortcuts import render
from numpy import number
project_list = [
    {'id':1,
    'title':"Ecommerce Website",
    'description':'Fully functional ecommerce website'},
    { 'id':2,
    'title':"Portfolio Website",
    'description':'This wasaproject whereIbuilt out my portfolio'},
    {'id':3,
    'title':"Social Network",
    'description':'Awesome open source projectIam still working on'}
]
    
   
    
# Create your views here.
def projects(request):
    msg = 'hello, you are on projects page'
    number = 11
    context = {'msg':msg,'number':number,'projectlist':project_list}
    return render(request,'mainApp/projects.html',context)

def mainpage(request):
    return render(request,'main.html')

def project(request,pk):
    proj = None
    for i in project_list:
        if i['id'] == pk:
            proj = i
    return render(request,'mainApp/single-project.html',{'project':proj})