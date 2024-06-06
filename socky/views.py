from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from . models import *

consultants = Teacher.objects.all()
states = Theme.STATES
sections = Theme.SECTIONS


def index(request):

    if request.method == "GET":
        themes = Theme.objects.all()
    
        return render(request, "index.html", {"themes" : themes, 
                                            "consultants" : consultants,
                                            "states" : states,
                                            "sections" : sections})
    
    elif request.method == "POST":
        nameInput = request.POST.get("name", None)
        consultantInput = request.POST.get("consultant", None)
        sectionInput = request.POST.get("section", None)
        stateInput = request.POST.get("state", None)

        filters = {
            "name": nameInput,
            "consultant": consultantInput,
            "section": sectionInput,
            "state": stateInput,
        }

        filters = {key: value for key, value in filters.items() if value not in (None, '')}

        themes = Theme.objects.filter(**filters)

        print(filters)
        print(themes)

        return render(request, "index.html", {
            "themes" : themes,
            "consultants" : consultants,
            "sections" : sections,
            "states" : states
        })

        