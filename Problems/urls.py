from django.urls import path, include
from . import views
from django.views.generic import ListView, DetailView
from .models import Task

urlpatterns = [
    path('', views.allTasks, name='problems'),
    # path('', ListView.as_view(queryset=Task.objects.all().order_by("-date")[:20], template_name="Problems/tasks.html")),
    # path('<int:pk>/', DetailView.as_view(model=Task, template_name='Problems/task.html')),
]