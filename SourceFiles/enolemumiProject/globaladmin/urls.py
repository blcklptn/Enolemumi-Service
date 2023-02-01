from django.urls import path
from . import views

urlpatterns: list = [
    path('globaladmin', views.globaladminPage, name='globaladmin'),
    path('globaladmin_statistic', views.globaladminStatistic, name='globaladmin')
]