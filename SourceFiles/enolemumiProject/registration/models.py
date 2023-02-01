from django.db import models

# Create your models here.
class MyUsers(models.Model):
    fullName = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    role = models.CharField(max_length=100, default='Пользователь')