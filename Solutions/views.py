from django.shortcuts import render
from . import forms
from Problems import models
from django.shortcuts import HttpResponse
import runProgram

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
        # if form.is_valid():
        # solution  = request.POST['solution']
        dict = {"form" : form}
        dict['success'] = True
        dict['successing'] ='Form submitted'

        # todo save program to file
        # runProgram.runFile("C:/projects/myleetcode/a.py", 60)
        return render(request, "Solutions/checksoltrue.html", dict)
        # else:
        #     dict ={}
        #     return render(request, "Solutions/checksolfalse.html", dict)
        # result = runpy._run_code(code=form, run_globals=None, mod_name=None,mod_spec=None, pkg_name=None, script_name=None)
        # if models.Task.realsolution == result:
        #     return render(request, 'Solutions/checksoltrue.html')
        # else:
        #     return render(request, 'Solutions/checksolfalse.html')
    # elif request.method == "GET":
    #     return render(request, "Solutions/sol.html")

# Create your views here.
# создать список задач на которые надо будет нажимать и вводить ответ, форма для решения не должна появлятся просто так а только после нажатия на вопрос после которого переадресация на форму
# нужно связать форму с views