from django.shortcuts import render

# Create your views here.

def start(request):
    return render(request, 'home/start/index.html',)

def registration(request):
    return render(request, 'home/Registration/index.html',)