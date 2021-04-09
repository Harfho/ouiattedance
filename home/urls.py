from django.urls import path
from . import views


app_name = 'home'
urlpatterns = [
    path('', views.start, name='start'),
    path('registration', views.registration, name='registration'),
]
