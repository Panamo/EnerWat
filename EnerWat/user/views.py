from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login as django_login
from .forms import LoginForm
from .forms import SignupModelForm
from .models import User


# Create your views here.
def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {'form': SignupModelForm()})
    if request.method == 'POST':
        form = SignupModelForm(request.POST)

        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            university = form.cleaned_data['university']
            major = form.cleaned_data['major']

            user = User.objects.create_user(email, email, password, first_name=first_name, last_name=last_name,
                                            phone_number=phone_number, university=university, major=major)
            user.save()
            return HttpResponseRedirect('signup_valid')


def login(request):
    if request.method == 'GET':
        return render(request, 'signin.html',{
            'false_user' : False
        })
    if request.method == 'POST':
        form = LoginForm(request.POST)

        email_empty = False
        password_empty = False
        false_user = False

        if form.is_valid():
            username = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user:
                django_login(request, user)
                return HttpResponseRedirect('/user')
            else:
                false_user = True
                return render(request, 'signin.html', {
                    'false_user':false_user
                }) # render login page with errors
        else:
            if not request.POST.get('email', None):
                email_empty = True
            if not request.POST.get('password', None):
                password_empty = True
            
            return render(request, 'signin.html', {
                'password_empty' : password_empty,
                'email_empty' : email_empty
            }) # render login page with errors
    else:
        return HttpResponseRedirect('/kire_khar')
