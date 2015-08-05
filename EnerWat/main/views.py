from django.shortcuts import render
from django.views.generic.base import View
from user.forms import LoginForm


# Create your views here.
class MainView(View):
    template_name = 'main/index.html'

    def get(self, request):
        login_model_form = LoginForm()
        return render(request, self.template_name, {
            'form': login_model_form
        })


class ContactView(View):
    template_name = 'main/contact.html'

    def get(self, request):
        return render(request, self.template_name)
