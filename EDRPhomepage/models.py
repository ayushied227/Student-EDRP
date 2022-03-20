from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=100)
    division=models.CharField(max_length=100, default='9A4', blank=True)
    subject=models.CharField(max_length=100, null=True)
    subjectteacher=models.CharField(max_length=100, null=True)


    def __str__(self):
        return self.name

class Subject(models.Model):
    TERMINALEXAM = "TERMINALEXAM"
    MONDAYTEST = "MONDAYTEST"
    ANNUALEXAM = "ANNUALEXAM"
    HOMEASSIGNMENT = "HOMEASSIGNMENT"
    LABWORK = "LABWORK"
    
    testtype=(
        (TERMINALEXAM, "TERMINALEXAM"),
        (MONDAYTEST, "MONDAYTEST"),
        (ANNUALEXAM, "ANNUALEXAM"),
        (HOMEASSIGNMENT, "HOMEASSIGNMENT"),
        (LABWORK, "LABWORK"),
    )
    scorecard=models.ForeignKey(User, on_delete=models.CASCADE)
    test=models.CharField(max_length=30, default = HOMEASSIGNMENT, choices=testtype)

