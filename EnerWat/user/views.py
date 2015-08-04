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
            title = form.cleaned_data['title']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            mobile_number = form.cleaned_data['mobile_number']
            education = form.cleaned_data['education']
            degree = form.cleaned_data['degree']
            field_of_study = form.cleaned_data['field_of_study']
            reg_type = form.cleaned_data['reg_type']
            country = form.cleaned_data['country']
            city = form.cleaned_data['city']
            postal_address = form.cleaned_data['postal_address']
            photo = request.FILES.get('photo', None)

            user = User.objects.create_user(email, email, password, title=title, first_name=first_name,
                                            last_name=last_name,
                                            phone_number=phone_number, mobile_number=mobile_number,
                                            degree=degree, education=education, field_of_study=field_of_study,
                                            reg_type=reg_type, country=country, city=city,
                                            postal_address=postal_address, photo=photo)
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
            username = form.cleaned_data['email']
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
            return render(request, 'signin.html', {
                'password_empty': password_empty,
                'email_empty': email_empty
            })
