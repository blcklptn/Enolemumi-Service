from django.shortcuts import render, redirect
from . import grabbers
from enolemumiProject.settings import SITES
from .models import Cases
from datetime import datetime
global last_run, parser_status
last_run = '02.02.2023'
parser_status = 'stopped'
# Create your views here.
def globaladminPage(request: object) -> render:
    if request.session['email']:
        print(request.session['email'])
        return render(request, 'enolemumi/globalAdminPage.html', {'name': request.session['full_name'], 'email': request.session['email']})
    else:
        return redirect('login')


def get_database_statistic():
    count_of_cases = Cases.objects.count()
    count_of_new_cases = Cases.objects.filter(last_parsed=str(datetime.now().strftime("%m/%d/%Y"))).count()
    average_count_of_cases = int(count_of_cases / count_of_new_cases)
    data_tuple = [count_of_cases, count_of_new_cases, average_count_of_cases]
    return data_tuple

def globaladminStatistic(request: object) -> render:
    if request.session['email']:
        data = get_database_statistic()
        return render(request, 'enolemumi/Statistic.html', {
                    'name': request.session['full_name'],
                    'email': request.session['email'],
                    'parser_status': parser_status,
                    'parser_last_run': last_run,
                    'parser_last_document': '01.02.2023',
                    'parser_percent_of_errors': '1%',
                    'parser_site': 'https://enonolemu.com',
                    'count_of_cases': data[0],
                    'count_of_new_cases': data[1],
                    'average_count_of_cases': data[2],
                    'sites': SITES['ptac_gov']
                })
    else:
        return redirect('')


def userEdit(request: object) -> render:
    if request.session['email']:
        return render(request, 'enolemumi/UserEdit.html', {'name': request.session['full_name'], 'email': request.session['email']}) 
    else:
        return redirect('login')

def logout(request: object) -> render:
    if request.session['email']:
        del request.session['email']
        del request.session['full_name']
        return redirect('login')
    return redirect('login')

def startParse(request: object) -> render:
    global last_run, parser_status
    if request.session['email']:
        parser_status = 'Work'
        grabbers.Run().run()
        print(request.POST)
        parser_status = 'Done'
        last_run = str(datetime.now().strftime("%m/%d/%Y"))
        return render(request, 'enolemumi/Statistic.html', {'name': request.session['full_name'], 'email': request.session['email']})
    else:
        return redirect('login')