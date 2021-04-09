from django.shortcuts import render

# Create your views here.


def login(request):
    return render(request, 'teachers/loginTeacher.html',)
def register(request):
    return render(request, 'teachers/registerTeacher.html',)
