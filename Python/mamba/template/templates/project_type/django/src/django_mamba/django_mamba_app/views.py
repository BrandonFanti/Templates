from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'landing.html')

def login(request):
    return render(request, 'login.html')