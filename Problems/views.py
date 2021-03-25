from django.shortcuts import render

import ResultSaver
from .models import Task
from Solutions import forms
import programRunner
from datetime import datetime

from django.views.generic import ListView, DetailView

class CheckResult:
    def __init__(self, expected, actual, success:bool, inputTask):
        self.success = success
        self.expected = expected
        self.actual = actual
        self.inputTask = inputTask

def allTasks(request):
    tasks = Task.objects.order_by('date')[:50]
# todo тут надо бы сделать так чтобы остальные после первых 50 тоже показывались но на следующей странице
    dict ={
        'tasks':tasks
    }
    return render(request, 'Problems/tasks.html', dict)

def saveToFile(userClass: str, task:Task, date:str):
    pythonClassTemplate = task.realsolution
    pythonClassTemplate = pythonClassTemplate.replace("//userclass//", userClass)
    pythonClassTemplate = pythonClassTemplate.replace("//userdate//", date)
    finalClass = pythonClassTemplate
    filename = "C:/projects/myleetcode/" + date + str('.py')
    file = open(filename, "w+")
    file.write(finalClass)
    file.close()
    return filename

def checkSolution(resultFileName: str) -> CheckResult :
    file = open(resultFileName, "r")
    for line in file:
        if line.startswith("false"):
            results = line.split(";")
            return CheckResult(results[1], results[2], False,results[3])
    file.close()
    return CheckResult("", "", True,"")

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
        task = Task.objects.get(id=pk)
        form = forms.SolForm(request.POST)
        data = form.data['textarea']

        now = datetime.now().strftime("%Y%m%d%H%M%S")
        pythonFileName = saveToFile(data, task, now)
        runner = programRunner.ProgramRunner()
        runner.runFile(pythonFileName, 0)
        resultFileName = ResultSaver.ResultSaver.getResultName(now)

        checkResult = checkSolution(resultFileName)
        rememberedID = request.session.get('remembered')
        dict = {"data" : data}
        dict["elem"] = task
        dict['realsolution'] = task.realsolution
        dict['rememberedID'] = rememberedID
        dict['checkSol'] = checkResult
        return render(request, "Problems/checksol.html", dict)



