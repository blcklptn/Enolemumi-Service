from django.contrib import admin
from .models import MyUsers
# Register your models here.
@admin.register(MyUsers)
class RequestDemoAdmin(admin.ModelAdmin):
  list_display = ['fullName', 'email', 'password']