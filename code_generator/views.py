from django.shortcuts import render
from django.db import IntegrityError
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import User
from django.db.models import Sum

# Create your views here.


def index(request):
    if request.method == 'GET':
        if request.user is not None and request.user.is_superuser:
            return render(request, 'code_generator/index.html')


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/code_generator/login/')


def index(request):
    if request.method == 'GET':
        if request.user is not None and request.user.is_superuser:
            return render(request, 'code_generator/index.html')


def index(request):
    if request.method == 'GET':
        if request.user is not None and request.user.is_superuser:
            return render(request, 'code_generator/index.html')


def index(request):
    if request.method == 'GET':
        if request.user is not None and request.user.is_superuser:
            return render(request, 'code_generator/index.html')


def index(request):
    if request.method == 'GET':
        if request.user is not None and request.user.is_superuser:
            return render(request, 'code_generator/index.html')
# 404 page ############################################################################################


def handler404(request, exception):
    response = render(request, 'code_generator/404.html')
    response.status_code = 404
    return response


def handler500(request):
    response = render(request, 'code_generator/404.html')
    response.status_code = 500
    return response
