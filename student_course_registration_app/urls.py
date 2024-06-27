from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('register_student/', views.register_student, name='register_student'),
    path('register_course/', views.register_course, name='register_course'),
    path('student_list/<int:course_id>/', views.student_list, name='student_list'),
]
