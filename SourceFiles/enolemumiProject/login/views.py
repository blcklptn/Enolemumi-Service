from django.shortcuts import render, redirect
from registration.models import MyUsers

# Create your views here.
def login(request: object) -> render:
    print('qweqwe')
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        userEx = MyUsers.objects.filter(email=email).exists()
        if userEx:
            user = MyUsers.objects.get(email=email)
            if password == user.password:
                print('Login!')
                return redirect('/')
            else:
                return render(request, 'enolemumi/login.html')

        else:
            return render(request, 'enolemumi/login.html')
        return redirect('/')

    else:
        return render(request, 'enolemumi/login.html')
