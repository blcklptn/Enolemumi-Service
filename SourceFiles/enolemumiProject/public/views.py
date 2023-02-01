from django.shortcuts import render

# Create your views here.
def index(request: object) -> render:
    return render(request, 'enolemumi/index.html')