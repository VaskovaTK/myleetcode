from django.shortcuts import render

def firstPage(request):
    return render(request, 'mainPage/mainPage.html')
# Create your views here.
def contacts(request):
    return render(request, 'mainPage/contacts.html')

# Create your views here.
