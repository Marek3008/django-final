from django.shortcuts import render, redirect
from . models import *




def index(request):

    themes = Theme.objects.all()
    consultants = Teacher.objects.all()
    states = State.objects.all()
    sections = Section.objects.all()

    return render(request, "index.html", {
        "themes" : themes, 
        "consultants" : consultants,
        "states" : states,
        "sections" : sections
    })

def create(request):

    availableStudents = []
    consultants = Teacher.objects.all()
    students = Student.objects.all()

    for i in students:
        if not Theme.objects.filter(student=i).exists():
            availableStudents.append(i)

    states = State.objects.all()
    sections = Section.objects.all()


    if request.method == "POST":

        if request.POST.get("student") != "":
            global student
            student = Student.objects.get(pk=request.POST.get("student"))
        
        else:
            student = None

        teacher = Teacher.objects.get(pk=request.POST.get("consultant"))
        section = Section.objects.get(pk=request.POST.get("section"))
        state = State.objects.get(pk=1) if student == None else State.objects.get(pk=2)

        

        Theme(
            name=request.POST.get("name"),
            description=request.POST.get("description"),
            state=state,
            consultant=teacher,
            student=student,
            consNum=0,
            section=section
        ).save()

        return redirect("index")

    return render(request, "create.html", {
        "consultants" : consultants,
        "states" : states,
        "sections" : sections,
        "students" : availableStudents
    })

def teacher(request, id):

    teacher = Teacher.objects.get(pk=id)
    themes = Theme.objects.filter(consultant=teacher)

    return render(request, "person.html", {
        "teacher" : teacher,
        "themes" : themes
    })

def student(request, id):

    student = Student.objects.get(pk=id)
    theme = Theme.objects.get(student=student)

    return render(request, "person.html", {
        "student" : student,
        "theme" : theme
    })   

def statistics(request):

    teachers = Teacher.objects.count()
    students = Student.objects.count()
    themes = Theme.objects.count()
    availableThemes = Theme.objects.filter(state=State.objects.get(pk=1)).count()
    unavailableThemes = Theme.objects.filter(state=State.objects.get(pk=2)).count()
    pendingThemes = Theme.objects.filter(state=State.objects.get(pk=3)).count()

    return render(request, "statistics.html", {
        "teachers" : teachers,
        "students" : students,
        "themes" : themes,
        "availableThemes" : availableThemes,
        "unavailableThemes" : unavailableThemes,
        "pendingThemes" : pendingThemes
    })