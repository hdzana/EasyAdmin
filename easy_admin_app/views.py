from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .printing import MyPrint
from io import BytesIO
from .models import *
from itertools import chain
'''
def index(request):
    return redirect('/admin')
    '''

def index(request):
	return render(request, 'easy_admin_app/index.html')

def welcome(request):
	return render(request, 'easy_admin_app/welcome.html')


def filter(request):
    if request.GET.get('programmes_btn'):
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="odsjeci.pdf"'
        buffer = BytesIO()
        _report = MyPrint(buffer)
        name = (request.GET.get('programme')).encode('utf-8')

        pdf = _report.generate_report_programmes(str(name))
        response.write(pdf)
        return response

    elif request.GET.get('employees_btn'):
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="uposlenici.pdf"'
        buffer = BytesIO()
        _report = MyPrint(buffer)

        sortId = (request.GET.get('employees')).encode('utf-8')
        if sortId == 'Alphabetical order':
            sortId = 1
        elif sortId == 'Occupation':
            sortId = 2

        pdf = _report.generate_report_employee(int(sortId))
        response.write(pdf)
        return response
        
    elif request.GET.get('students_btn'):
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="studenti.pdf"'
        buffer = BytesIO()
        _report = MyPrint(buffer)

        sortId = (request.GET.get('students')).encode('utf-8')
        if sortId == 'Alphabetical order':
            sortId = 1
        elif sortId == 'Programme of study':
            sortId = 2
        elif sortId == 'Municipality of birth':
            sortId = 3
   
        pdf = _report.generate_report_child(int(sortId))
        response.write(pdf)
        return response

    return render(request, "easy_admin_app/report.html")