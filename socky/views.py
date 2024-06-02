from django.shortcuts import render
from . models import *


consultants = Teacher.objects.all()
themes = Theme.objects.all()
states = Theme.STATES
sections = Theme.SECTIONS



def index(request):
    return render(request, "index.html", {"themes" : themes, 
                                          "consultants" : consultants,
                                          "states" : states,
                                          "sections" : sections})
