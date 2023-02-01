from django.shortcuts import render
from .models import MyUsers
from django.shortcuts import redirect

# Create your views here.
def registration(request: object) -> render:
    if request.method == 'GET':
        return render(request, 'enolemumi/reg.html')
    else:
        users = MyUsers.objects.create(fullName=request.POST['full_name'], email=request.POST['email'], password=request.POST['password'])
        users.save()
        return redirect('/login/')