from django.shortcuts import render

# Create your views here.
def registration(request: object) -> render:
    return render(request, 'enolemumi/reg.html')