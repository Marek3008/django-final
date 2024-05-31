from django.shortcuts import render
from . models import *

def index(request):
    return render(request, "socky/index.html", {"themes" : Theme.objects.all()})
