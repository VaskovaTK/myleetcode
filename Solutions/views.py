from django.shortcuts import render
from . import forms
from Problems import models as modelTask
from django.shortcuts import HttpResponse
import runProgram
import saveToFile

# def sol(request):
#     return render(request, 'Solutions/sol.html')
#
# def solved(request, pk):
    # if request.method =="GET":
    #     form = forms.SolForm()
    #     dict = { 'form': form,
    #              'pk': str(pk)
    #     }
    #     return render(request, 'Solutions/solved.html', context= dict)
    # elif request.method =="POST":
    #     session = request.session['session']
    #     task = modelTask.Task.objects.filter(id=pk)
    #     form = forms.SolForm(request.POST)
    #     data = form.data['textarea']
    #     save = saveToFile.Save()
    #     filePath = save.saveToFile(data)
    #     run = runProgram.RunProgram()
    #     afterRun = run.runFile(filePath, 0)
    #     dict = {"data" : data}
    #     dict['afterRun'] = afterRun
    #     dict["task"] = task
    #     dict['session'] = session
    #     # todo сравнивать значения с realsolution
    #     return render(request, "Solutions/checksol.html", dict)
