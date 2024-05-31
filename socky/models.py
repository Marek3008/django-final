from django.db import models



class Class(models.Model):

    name = models.CharField(max_length=6)


class Student(models.Model):

    className = models.ForeignKey(Class, on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=10)
    surname = models.CharField(max_length=15)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=40)


class Teacher(models.Model):

    name = models.CharField(max_length=10)
    surname = models.CharField(max_length=15)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=40)


class Theme(models.Model):

    STATES = (
        ("available", "Available"),
        ("unavailable", "Unavailable"),
        ("pending", "Pending")
    )

    consultant = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=40)
    description = models.TextField()
    state = models.CharField(max_length=11, choices=STATES)
    consNum = models.IntegerField(default=0)