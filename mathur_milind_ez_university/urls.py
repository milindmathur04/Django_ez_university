"""mathur_milind_ez_university URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from courseinfo.views import (instructor_list_view, section_list_view, semester_list_view, student_list_view,
                              course_list_view, registration_list_view)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('instructor/', instructor_list_view),
    path('section/', section_list_view),
    path('semester/', semester_list_view),
    path('student/', student_list_view),
    path('course/', course_list_view),
    path('registration/', registration_list_view),
]
