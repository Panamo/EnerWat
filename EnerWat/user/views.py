from django.shortcuts import render
from django.shortcuts import redirect
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
        form = SignupModelForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']

            user = User.objects.create_user(username, email, password, first_name=first_name,
                                            last_name=last_name)
            user.save()
            return redirect('/')
        else:
            return render(request, self.template_name, {'form': form})


class UserLogin(View):
    template_name = 'user/login.html'

    def get(self, request):
        return render(request, self.template_name, {'form': LoginForm()})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user:
                django_login(request, user)
                return redirect('user_detail', pk=user.pk)
            else:
                return render(request, self.template_name, {'form': form})
        else:
            return render(request, self.template_name, {'form': form})
