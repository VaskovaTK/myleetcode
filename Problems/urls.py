from django.urls import path, include
from . import views
from django.views.generic import ListView, DetailView
from .models import Task
from Solutions import views as viewSol

urlpatterns = [
    path('', views.allTasks, name='problems'),
    # path('<int:pk>/',DetailView.as_view(model=Task, template_name='Problems/task.html')),
    path('<int:pk>/', views.task, name ='task'),
    path('solutions', viewSol.sol, name='solutions'),
    path('solved', viewSol.solved, name='solved'),
]
