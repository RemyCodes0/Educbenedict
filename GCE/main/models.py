from django.db import models
from django.contrib.auth.models import User

# Create your models here.
"""class Series(models.Model):
   SUBJECTS = [
        ("Chemistry", "Chemistry"),
        ("Biology", "Biology"),
        ("Physics", "Physics"),
        ("Further Mathematics", "Further Mathematics"),
        ("Mathematics","Mathematics"),
        ("Computer Science", "Computer Science"),
        ("ICT","ICT")
        ]
    SERIES_TYPES =[
        ("Science", "Science"),
        ("Artist","Artist")
    ]
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    series_choice = models.CharField(choices=SERIES_TYPES, max_length = 64)"""
class Subject(models.Model):
    
    title = models.CharField(max_length = 64)
    science = models.BooleanField(default = False, blank = False)
    art= models.BooleanField(default= False, blank = False)
    ordinary = models.BooleanField(default= False, blank = False)
    advanced =models.BooleanField(default= False, blank = False)

    def __str__(self):
        return self.title

class Year(models.Model):
    subject = models.ForeignKey(Subject, on_delete= models.CASCADE)
    title = models.CharField(max_length = 64)

    def __str__(self):
        return self.title

class Question(models.Model):
    subject = models.ForeignKey(Year, on_delete = models.CASCADE)
    PAPER = (
        ('Paper 1','Paper 1'),
        ('Paper 2', "Paper 2"),
        ('Paper 3', "Paper 3"),
    )
    paper = models.CharField(max_length = 20, choices = PAPER, default = "Paper 1")
    question = models.TextField()

    def __str__(self):
        return self.question
    
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete= models.CASCADE)
    answer = models.CharField(max_length= 100000)
    correct = models.BooleanField(default=False)
    
    def __str__(self):
        return self.answer