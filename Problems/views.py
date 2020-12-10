from django.shortcuts import render
from .models import Task

def allTasks(request):
    tasks = Task.objects.order_by('date')[:50]
    dict ={
        'tasks':tasks
    }
    return render(request, 'Problems/tasks.html', dict)




# # Create your views here.
