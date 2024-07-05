from django.contrib import admin
from .models import Course, Student  # Use capitalized model names


admin.site.register(Course)
admin.site.register(Student)
