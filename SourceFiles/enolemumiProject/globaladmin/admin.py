from django.contrib import admin
from .models import Cases, ParsingStatus

# Register your models here.
@admin.register(Cases)
class RequestDemoAdmin(admin.ModelAdmin):
  list_display = ['path_to_file', 'classification', 'site', 'last_parsed']

@admin.register(ParsingStatus)
class RequestDemoAdmin(admin.ModelAdmin):
  list_display = ['status', 'last_parsed', 'site']