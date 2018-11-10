from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, DeleteView, UpdateView

from courseinfo.utils import PageLinksMixin
from .models import (Instructor, Section, Course, Semester, Student, Registration)
from courseinfo.forms import InstructorForm, SectionForm, SemesterForm, StudentForm, CourseForm, RegistrationForm


class InstructorList(PageLinksMixin, ListView):
    paginate_by = 25
    model = Instructor


class InstructorDetail(View):
    def get(self, request, pk):
        instructor = get_object_or_404(
            Instructor,
            pk=pk
        )
        section_list = instructor.sections.all()
        return render(
            request,
            'courseinfo/instructor_detail.html',
            {'instructor': instructor, 'section_list': section_list}
        )


class InstructorCreate(CreateView):
    form_class = InstructorForm
    model = Instructor


class InstructorUpdate(UpdateView):
    form_class = InstructorForm
    model = Instructor
    template_name = 'courseinfo/instructor_form_update.html'


class InstructorDelete(DeleteView):
    model = Instructor
    success_url = reverse_lazy('courseinfo_instructor_list_urlpattern')


class SectionList(ListView):
    model = Section


class SectionDetail(View):
    def get(self, request, pk):
        section = get_object_or_404(
            Section,
            pk=pk
        )
        semester = section.semester
        course = section.course
        instructor = section.instructor
        registration_list = section.registrations.all()
        return render(
            request,
            'courseinfo/section_detail.html',
            {
                'section': section,
                'semester': semester,
                'course': course,
                'instructor': instructor,
                'registration_list': registration_list
            }
        )


class SectionCreate(CreateView):
    form_class = SectionForm
    model = Section


class SectionUpdate(UpdateView):
    form_class = SectionForm
    model = Section
    template_name = 'courseinfo/section_form_update.html'


class SectionDelete(DeleteView):
    model = Section
    success_url = reverse_lazy('courseinfo_section_list_urlpattern')


class SemesterList(ListView):
    model = Semester


class SemesterDetail(View):
    def get(self, request, pk):
        semester = get_object_or_404(
            Semester,
            pk=pk
        )
        section_list = semester.sections.all()
        return render(
            request,
            'courseinfo/semester_detail.html',
            {'semester': semester, 'section_list': section_list}
        )


class SemesterCreate(CreateView):
    form_class = SemesterForm
    model = Semester


class SemesterUpdate(UpdateView):
    form_class = SemesterForm
    model = Semester
    template_name = 'courseinfo/semester_form_update.html'


class SemesterDelete(DeleteView):
    model = Semester
    success_url = reverse_lazy('courseinfo_semester_list_urlpattern')


class StudentList(PageLinksMixin, ListView):
    paginate_by = 25
    model = Student


class StudentDetail(View):
    def get(self, request, pk):
        student = get_object_or_404(
            Student,
            pk=pk
        )
        registration_list = student.registrations.all()
        return render(
            request,
            'courseinfo/student_detail.html',
            {'student': student, 'registration_list': registration_list}
        )


class StudentCreate(CreateView):
    form_class = StudentForm
    model = Student


class StudentUpdate(UpdateView):
    form_class = StudentForm
    model = Student
    template_name = 'courseinfo/student_form_update.html'


class StudentDelete(DeleteView):
    model = Student
    success_url = reverse_lazy('courseinfo_student_list_urlpattern')


class CourseList(ListView):
    model = Course


class CourseDetail(View):
    def get(self, request, pk):
        course = get_object_or_404(
            Course,
            pk=pk
        )
        section_list = course.sections.all()
        return render(
            request,
            'courseinfo/course_detail.html',
            {'course': course, 'section_list': section_list}
        )


class CourseCreate(CreateView):
    form_class = CourseForm
    model = Course


class CourseUpdate(UpdateView):
    form_class = CourseForm
    model = Course
    template_name = 'courseinfo/course_form_update.html'


class CourseDelete(DeleteView):
    model = Course
    success_url = reverse_lazy('courseinfo_course_list_urlpattern')


class RegistrationList(ListView):
    model = Registration


class RegistrationDetail(View):
    def get(self, request, pk):
        registration = get_object_or_404(
            Registration,
            pk=pk
        )
        student = registration.student
        section = registration.section
        return render(
            request,
            'courseinfo/registration_detail.html',
            {
                'registration': registration,
                'section': section,
                'student': student
            }
        )


class RegistrationCreate(CreateView):
    form_class = RegistrationForm
    model = Registration


class RegistrationUpdate(UpdateView):
    form_class = RegistrationForm
    model = Registration
    template_name = 'courseinfo/registration_form_update.html'


class RegistrationDelete(DeleteView):
    model = Registration
    success_url = reverse_lazy('courseinfo_registration_list_urlpattern')
