from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    name=models.CharField(blank=False,max_length=100)

    age=models.IntegerField(blank=False)

    program=models.CharField(blank=True, default='BTech', max_length=100)
    
    subject=models.CharField(blank=False, max_length=50)

    tech=models.TextField(blank=False)

    addmission_date=models.DateTimeField(auto_now_add=True)

    mentor=models.ForeignKey(User, on_delete=models.CASCADE) #the student will also get deleted if the user is deleted, this is one way that is if user is deleted than student is deleted not vice versa

    def __str__(self): #used to return the name of the Student, this is returned in quesry set when running Student.objects.all() query
        return self.name