from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login

#Utility

def return_redirect(route):
    return HttpResponseRedirect(reverse(route))

def get_login_landing_page(user):
    return ''

#Actual views

def index(request):
    if request.user and not request.user.is_anonymous:
        user = request.user
        return render(request, 'landing.html', context={'user_first_name':user.first_name})
    return render(request, 'landing.html')

def user_login(request):
    if request.POST:
        username = request.POST['user']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/')
    return render(request, 'login.html')