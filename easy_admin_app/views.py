from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
'''
def index(request):
    return redirect('/admin')
    '''

def index(request):
	return render(request, 'easy_admin_app/index.html')

def welcome(request):
	return render(request, 'easy_admin_app/welcome.html')