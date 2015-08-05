from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.views.generic.base import View

from .forms import LoginForm
from .forms import SignupModelForm
from .models import User


# Create your views here.

class UserDetailView(DetailView):
    model = User

    def dispatch(self, request, *args, **kwargs):
        kwargs.update({'pk': str(request.user.pk)})
        self.kwargs.update({'pk': str(request.user.pk)})
        return super(UserDetailView, self).dispatch(request, *args, **kwargs)


class StaffListView(ListView):
    model = User
    template_name = 'user/staff_list.html'


class UserSignup(FormView):
    template_name = 'user/signup.html'
    form_class = SignupModelForm
    success_url = '/'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        password = form.cleaned_data['password']
        email = form.cleaned_data['email']

        user = User.objects.create_user(username, email, password, first_name=first_name,
                                        last_name=last_name)
        user.save()
        return super(UserSignup, self).form_valid(form)


class UserLogin(FormView):
    template_name = 'user/login.html'
    form_class = LoginForm

    def get_initial(self):
        kwargs = super(UserLogin, self).get_initial()
        next_url = self.request.GET.get('next', None)
        if next_url:
            kwargs.update({'next': next_url})
            print(next_url)
        return kwargs

    def form_valid(self, form):
        next_url = form.cleaned_data.get('next', None)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        print(next_url)

        user = authenticate(username=username, password=password)
        if user and not next_url:
            login(self.request, user)
            return redirect('user_detail')
        elif user and next_url:
            login(self.request, user)
            return redirect(next_url)
        else:
            return render(self.request, self.template_name, {'form': form})


class UserLogout(View):
    def get(self, request):
        if request.user.is_authenticated():
            logout(request)
        return redirect('home')
