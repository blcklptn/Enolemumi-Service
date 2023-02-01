from django.shortcuts import render

# Create your views here.
def globaladminPage(request: object) -> render:
    if request.session['email']:
        print(request.session['email'])
        return render(request, 'enolemumi/globalAdminPage.html', {'name': request.session['full_name'], 'email': request.session['email']})
    else:
        return redirect('login')

def globaladminStatistic(request: object) -> render:
    if request.session['email']:
        return render(request, 'enolemumi/Statistic.html', {'name': request.session['full_name'], 'email': request.session['email']})


def userEdit(request: object) -> render:
    if request.session['email']:
        return render(request, 'enolemumi/UserEdit.html', {'name': request.session['full_name'], 'email': request.session['email']}) 