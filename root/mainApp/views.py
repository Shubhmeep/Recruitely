from re import L
from django.http import HttpResponse
from django.shortcuts import redirect, render
from matplotlib.style import context
from numpy import number
from mainApp.models import project as pp
from .forms import ProjectForm
    
# Create your views here.
def projects(request):
    projectlist = pp.objects.all()
    context = {'projectlist':projectlist}
    return render(request,'mainApp/projects.html',context)

def mainpage(request):
    return render(request,'main.html')

def project(request,pk):
    projectlist = pp.objects.get(id=pk)
    tags = projectlist.tags.all()
    return render(request,'mainApp/single-project.html',{'project':projectlist,'tags':tags})


def createProject(request):
    forms = ProjectForm()
    if request.method == 'POST':
        forms = ProjectForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('projects')
    context = {'form':forms}
    return render(request,"mainApp/project_form.html",context)


def updateProject(request,pk):
    projectlist = pp.objects.get(id=pk)
    forms = ProjectForm(instance=projectlist)

    if request.method == 'POST':
        forms = ProjectForm(request.POST,instance = projectlist)
        if forms.is_valid():
            forms.save()
            return redirect('projects')
    context = {'form':forms}
    return render(request,"mainApp/project_form.html",context)

def deleteProject(request,pk):
    project = pp.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    context = {'object':project}
    return render(request, "mainApp/delete_object.html",context)