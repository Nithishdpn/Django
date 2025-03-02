from django.db import models

class Course(models.Model):  # Capitalized model name
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name

class Student(models.Model):
    first_name = models.CharField(max_length=255, default='')
    last_name = models.CharField(max_length=255, default='')
    email = models.EmailField(unique=True, default='')
    courses = models.ManyToManyField(Course, related_name='students', blank=True)  # Correct reference to Course
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
