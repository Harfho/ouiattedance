from django.urls import path
from . import views


app_name = 'student'
urlpatterns = [
    path('login/', views.login, name='loginStudent'),
    path('register/', views.register, name='registerStudent'),
]
