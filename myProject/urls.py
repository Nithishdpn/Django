 
 
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('datetimeapp.urls')),
    path('', include('fourdate_timeapp.urls')),
    path('', include('listfruitapp.urls')),
    path('', include('portfolioapp.urls')),
    path('', include('student_course_registration_app.urls')),
]
