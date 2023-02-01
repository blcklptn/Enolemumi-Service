from django.shortcuts import render, redirect

# Create your views here.
def login(request: object) -> render:
    print('qweqwe')
    if request.method == 'POST':
        print('autheficated')
        return redirect('/')
    else:
        return render(request, 'enolemumi/login.html')
