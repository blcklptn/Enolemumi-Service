from django.urls import path
from . import views

urlpatterns: list = [
    path('registration', views.registration, name='registration')
]