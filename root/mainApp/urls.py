
from django.urls import path
from . import views

urlpatterns = [
    path('projects/',views.projects,name="projects"),
    path('',views.mainpage,name="mainpage"),
    path('project/<int:pk>/',views.project,name="singleproject"),

]
