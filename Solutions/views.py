from django.shortcuts import render
from . import forms
from Problems import models
from django.shortcuts import HttpResponse
import runProgram
import saveToFile

def sol(request):
    return render(request, 'Solutions/sol.html')
def solved(request):
    if request.method =="GET":
        form = forms.SolForm()
        dict = { 'form': form
        }
        return render(request, 'checksol.html', context= dict)
    elif request.method =="POST":
        form = forms.SolForm(request.POST)
        data = form.data['textarea']
        save = saveToFile.Save()
        filePath = save.saveToFile(data)
        run = runProgram.RunProgram()
        afterRun = run.runFile(filePath, 0)
        dict = {"data" : data}
        dict['afterRun'] = afterRun
        # todo стрим ничего не возвращает
        # todo подписать в данные свои значения переменных и сравнивать с realsolution
        return render(request, "Solutions/checksoltrue.html", dict)
