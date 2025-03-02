from django.shortcuts import render, redirect
from .models import Course, Student  # Ensure correct capitalization
from .forms import StudentForm, CourseForm

def index(request):
    courses = Course.objects.all()  # Correct capitalization
    return render(request, 'registration/index.html', {'courses': courses})

def register_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = StudentForm()
    return render(request, 'registration/register_student.html', {'form': form})

def register_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CourseForm()
    return render(request, 'registration/register_course.html', {'form': form})

def student_list(request, course_id):
    course = Course.objects.get(id=course_id)  # Correct capitalization
    students = course.students.all()
    return render(request, 'registration/student_list.html', {'students': students, 'course': course})
