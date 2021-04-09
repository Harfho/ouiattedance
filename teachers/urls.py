from django.urls import path
from . import views


app_name = 'teacher'
urlpatterns = [
    path('login/', views.login, name='loginTeacher'),
    path('register/', views.register, name='registerTeacher'),
]
