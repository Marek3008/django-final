from django.db import models



class Class(models.Model):

    name = models.CharField(max_length=6)


class Student(models.Model):

    className = models.ForeignKey(Class, on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=10)
    surname = models.CharField(max_length=15)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.name} {self.surname}"


class Teacher(models.Model):

    name = models.CharField(max_length=10)
    surname = models.CharField(max_length=15)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.name} {self.surname}"
    
class Section(models.Model):

    name = models.CharField(max_length=65)

    def __str__(self):
        return f"{self.name}"

class State(models.Model):

    name = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name}"


class Theme(models.Model):

    consultant = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True, blank=True)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, null=True, blank=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=40)
    description = models.TextField()
    consNum = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name}"