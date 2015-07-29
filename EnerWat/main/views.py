from django.shortcuts import render
from user.forms import LoginModelForm


# Create your views here.
def main(request):
    login_model_form = LoginModelForm()
    return render(request, 'index.html', {
        'form': login_model_form
    })
