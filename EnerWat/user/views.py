from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login as django_login
from .forms import LoginModelForm


# Create your views here.
def signup(request):
    if request.method == 'GET':
        pass
    if request.method == 'POST':
        pass


def login(request):
    if request.method == 'GET':
        pass
    if request.method == 'POST':
        form = LoginModelForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['email']
            password = form.cleaned.data['password']

            user = authenticate(username=username, password=password)
            if user:
                django_login(request, user)
                return HttpResponseRedirect('/user_valid')
            else:
                return HttpResponseRedirect('/user_invalid')
        else:
            return HttpResponseRedirect("/invalid_form")
    else:
        return HttpResponseRedirect('/invalid_method')
