from django.shortcuts import render
from django.http import HttpResponse
from .models import About_me


# Create your views here.
def home(request):
    return render(request, 'layouts/base.html', {})


def start(request):
    register = About_me.objects.all()
    return render(request, 'index.html', {'register': register})


def Delete(request):
    enough = About_me.objects.get()
    enough.delete()
    return render(request, 'index.html', {'enough': enough})
