from django.shortcuts import render
from django.http import HttpResponse
from .models import About_me


# Create your views here.
def home(request):
    return render(request, 'layouts/base.html', {})


def start(request):
    register = About_me.objects.create(document='1014218980', names='Eduard Nicolás',
                                       last_names='Sarmiento Herrera', address='Calle 69a 112a - 13',
                                       networks='www.linkedin.com/in/eduard-nicolás-sarmiento-herrera')
    return render(request, 'index.html', {'register': register})
