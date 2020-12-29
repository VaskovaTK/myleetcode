from django.shortcuts import render
from .models import Task
from Solutions import forms
import saveToFile
import runProgram

from django.views.generic import ListView, DetailView

def allTasks(request):
    tasks = Task.objects.order_by('date')[:50]
    dict ={
        'tasks':tasks
    }
    return render(request, 'Problems/tasks.html', dict)

def task (request, pk):
    task = Task.objects.filter(id=pk)
    request.session['remembered'] = pk
    if request.method =="GET":
        form = forms.SolForm()
        dict = { 'form': form,
                 'pk': pk,
                 'task': task,
        }
        return render(request, 'Problems/task.html', context= dict)
    elif request.method =="POST":
        task = Task.objects.filter(id=pk)
        form = forms.SolForm(request.POST)
        data = form.data['textarea']
        save = saveToFile.Save()
        filePath = save.saveToFile(data)
        run = runProgram.RunProgram()
        afterRun = run.runFile(filePath, 0)
        rememberedID = request.session.get('remembered')
        dict = {"data" : data}
        dict['afterRun'] = afterRun
        dict["task"] = task
        dict['rememberedID'] = rememberedID
        # todo сравнивать значения с realsolution
        return render(request, "Problems/checksol.html", dict)

    task = Task.objects.filter(id=pk)
    dict = {'task': task}
    return render(request, 'Problems/task.html', dict)

# todo может быть здесь брать содержимое realsolution у pk и записывать его в файл а потом сравнивать с решением пользователя


# # Create your views here.
