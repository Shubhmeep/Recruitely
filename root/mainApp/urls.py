
from django.urls import path
from . import views

urlpatterns = [
    path('',views.projects,name="projects"),
    #path('',views.mainpage,name="mainpage"),
    path('project/<str:pk>/',views.project,name="singleproject"),
    path('create-project/',views.createProject,name="create-project"),
    path('update-project/<str:pk>',views.updateProject,name="update-project")

]
