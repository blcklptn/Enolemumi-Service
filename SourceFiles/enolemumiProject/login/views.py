from django.shortcuts import render, redirect
from registration.models import MyUsers

# Create your views here.
def login(request: object) -> render:
    if request.session['email']:
        return redirect('/globaladmin')

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        userEx = MyUsers.objects.filter(email=email).exists()
        if userEx:
            user = MyUsers.objects.get(email=email)
            if password == user.password:
                role = user.role
                if role == 'Администратор':
                    print(request.session.session_key)
                    request.session['email'] = user.email
                    request.session['full_name'] = user.fullName
                    return redirect('/globaladmin')
                elif role == 'Пользователь':
                    pass
                
                print(f'Login! as {role}')
                return redirect('/')
            else:
                return render(request, 'enolemumi/login.html')

        else:
            return render(request, 'enolemumi/login.html')
        return redirect('/')

    else:
        return render(request, 'enolemumi/login.html')
