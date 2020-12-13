from django.shortcuts import render
from .models import Task
from django.views.generic import ListView, DetailView

def allTasks(request):
    tasks = Task.objects.order_by('date')[:50]
    dict ={
        'tasks':tasks
    }
    return render(request, 'Problems/tasks.html', dict)

def task (request, pk):
    task = Task.objects.filter(id=pk)
    dict = {'task': task}
    return render(request, 'Problems/task.html', dict)

# todo здесь запускать сравнение по персональному ключу в real solution с тем что лежит в отдельном файле user result
# todo может быть здесь брать содержимое realsolution у pk и записывать его в файл а потом сравнивать с решением пользователя


# # Create your views here.
