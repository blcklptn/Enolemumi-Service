from django.shortcuts import render

# Create your views here.
def login(request: object) -> render:
    return render(request, 'enolemumi/login.html')