from django.contrib import admin
from .models import Semester, Section, Course, Instructor, Student, Registration


admin.site.register(Semester)
admin.site.register(Section)
admin.site.register(Course)
admin.site.register(Instructor)
admin.site.register(Student)
admin.site.register(Registration)
