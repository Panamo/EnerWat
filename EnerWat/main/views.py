from django.shortcuts import render
from user.forms import LoginForm


# Create your views here.
def main(request):
    login_model_form = LoginForm()
    return render(request, 'index.html', {
        'form': login_model_form
    })
