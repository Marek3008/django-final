from django.urls import path
from . views import *

urlpatterns = [
    path('', index, name="index"),
    path('create/', create, name="create"),
    path('teacher/<int:id>', teacher, name="teacher"),
    path('student/<int:id>', student, name="student"),
    path('statistics/', statistics, name="statistics")
]
