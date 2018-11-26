from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from courseinfo.utils import PageLinksMixin
from .models import (Instructor, Section, Course, Semester, Student, Registration)
from courseinfo.forms import InstructorForm, SectionForm, SemesterForm, StudentForm, CourseForm, RegistrationForm


class InstructorList(LoginRequiredMixin, PermissionRequiredMixin, PageLinksMixin, ListView):
    paginate_by = 25
    model = Instructor
    permission_required = 'courseinfo.view_instructor'


class InstructorDetail(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'courseinfo.view_instructor'

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


class InstructorCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = InstructorForm
    model = Instructor
    permission_required = 'courseinfo.add_instructor'


class InstructorUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = InstructorForm
    model = Instructor
    template_name = 'courseinfo/instructor_form_update.html'
    permission_required = 'courseinfo.change_instructor'


class InstructorDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Instructor
    success_url = reverse_lazy('courseinfo_instructor_list_urlpattern')
    permission_required = 'courseinfo.delete_instructor'


class SectionList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Section
    permission_required = 'courseinfo.view_section'


class SectionDetail(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'courseinfo.view_section'

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


class SectionCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = SectionForm
    model = Section
    permission_required = 'courseinfo.add_section'


class SectionUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = SectionForm
    model = Section
    template_name = 'courseinfo/section_form_update.html'
    permission_required = 'courseinfo.change_section'


class SectionDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Section
    success_url = reverse_lazy('courseinfo_section_list_urlpattern')
    permission_required = 'courseinfo.delete_section'


class SemesterList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Semester
    permission_required = 'courseinfo.view_semester'


class SemesterDetail(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'courseinfo.view_semester'

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


class SemesterCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = SemesterForm
    model = Semester
    permission_required = 'courseinfo.add_semester'


class SemesterUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = SemesterForm
    model = Semester
    template_name = 'courseinfo/semester_form_update.html'
    permission_required = 'courseinfo.change_semester'


class SemesterDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Semester
    success_url = reverse_lazy('courseinfo_semester_list_urlpattern')
    permission_required = 'courseinfo.delete_semester'


class StudentList(LoginRequiredMixin, PermissionRequiredMixin, PageLinksMixin, ListView):
    paginate_by = 25
    model = Student
    permission_required = 'courseinfo.view_student'


class StudentDetail(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'courseinfo.view_student'

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


class StudentCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = StudentForm
    model = Student
    permission_required = 'courseinfo.add_student'


class StudentUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = StudentForm
    model = Student
    template_name = 'courseinfo/student_form_update.html'
    permission_required = 'courseinfo.change_student'


class StudentDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Student
    success_url = reverse_lazy('courseinfo_student_list_urlpattern')
    permission_required = 'courseinfo.delete_student'


class CourseList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Course
    permission_required = 'courseinfo.view_course'


class CourseDetail(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'courseinfo.view_course'

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


class CourseCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = CourseForm
    model = Course
    permission_required = 'courseinfo.add_course'


class CourseUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = CourseForm
    model = Course
    template_name = 'courseinfo/course_form_update.html'
    permission_required = 'courseinfo.change_course'


class CourseDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Course
    success_url = reverse_lazy('courseinfo_course_list_urlpattern')
    permission_required = 'courseinfo.delete_course'


class RegistrationList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Registration
    permission_required = 'courseinfo.view_registration'


class RegistrationDetail(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'courseinfo.view_registration'

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


class RegistrationCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = RegistrationForm
    model = Registration
    permission_required = 'courseinfo.add_registration'


class RegistrationUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = RegistrationForm
    model = Registration
    template_name = 'courseinfo/registration_form_update.html'
    permission_required = 'courseinfo.change_registration'


class RegistrationDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Registration
    success_url = reverse_lazy('courseinfo_registration_list_urlpattern')
    permission_required = 'courseinfo.delete_registration'
