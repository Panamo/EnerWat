from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login as django_login
from django.views.generic.detail import DetailView
from django.views.generic.base import View

from .forms import LoginForm
from .forms import SignupModelForm
from .models import User


# Create your views here.

class UserDetailView(DetailView):
    model = User


class UserSignup(View):
    template_name = 'user/signup.html'

    def get(self, request):
        return render(request, self.template_name, {'form': SignupModelForm()})

    def post(self, request):
        form = SignupModelForm(request.POST, request.FILES)

        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']

            user = User.objects.create_user(username, email, password, first_name=first_name,
                                            last_name=last_name)
            user.save()
            return HttpResponseRedirect('signup_valid')
        else:
            return render(request, self.template_name, {'form': form})


class UserLogin(View):
    template_name = 'user/login.html'

    def get(self, request):
        return render(request, self.template_name, {'form': LoginForm(), 'false_user': False})

    def post(self, request):
        form = LoginForm(request.POST)

        email_empty = False
        password_empty = False

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user:
                django_login(request, user)
                return HttpResponseRedirect('/user')
            else:
                false_user = True
                # render login page with errors
                return render(request, self.template_name, {'false_user': false_user})
        else:
            if not request.POST.get('email', None):
                email_empty = True
            if not request.POST.get('password', None):
                password_empty = True

            # render login page with errors
            return render(request, self.template_name, {
                'password_empty': password_empty,
                'email_empty': email_empty
            })
