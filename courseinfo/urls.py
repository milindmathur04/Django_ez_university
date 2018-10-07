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
from courseinfo.views import (InstructorList, SectionList, SemesterList, StudentList, CourseList, RegistrationList,
                              InstructorDetail, SectionDetail, RegistrationDetail, StudentDetail, SemesterDetail,
                              CourseDetail)

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('instructor/',
         InstructorList.as_view(),
         name='courseinfo_instructor_list_urlpattern'),
    path('instructor/<int:pk>/',
         InstructorDetail.as_view(),
         name='courseinfo_instructor_detail_urlpattern'),
    path('section/',
         SectionList.as_view(),
         name='courseinfo_section_list_urlpattern'),
    path('section/<int:pk>/',
         SectionDetail.as_view(),
         name='courseinfo_section_detail_urlpattern'),
    path('semester/',
         SemesterList.as_view(),
         name='courseinfo_semester_list_urlpattern'),
    path('semester/<int:pk>/',
         SemesterDetail.as_view(),
         name='courseinfo_semester_detail_urlpattern'),
    path('student/',
         StudentList.as_view(),
         name='courseinfo_student_list_urlpattern'),
    path('student/<int:pk>/',
         StudentDetail.as_view(),
         name='courseinfo_student_detail_urlpattern'),
    path('course/',
         CourseList.as_view(),
         name='courseinfo_course_list_urlpattern'),
    path('course/<int:pk>/',
         CourseDetail.as_view(),
         name='courseinfo_course_detail_urlpattern'),
    path('registration/',
         RegistrationList.as_view(),
         name='courseinfo_registration_list_urlpattern'),
    path('registration/<int:pk>/',
         RegistrationDetail.as_view(),
         name='courseinfo_registration_detail_urlpattern'),
]
