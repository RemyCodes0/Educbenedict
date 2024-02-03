from django.shortcuts import render
from django.views.generic.list import ListView
from . import models
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
# Create your views here.


class OwnerMixin:
    def get_queryset(self):
        qs = super().get_queryset() # type: ignore
        return qs.filter(user = self.request.user) # type: ignore
    
class OwnerEditMixin:
    def form_valid(self, form):
        form.instance.user = self.request.user # type: ignore
        return super().form_valid(form) # type: ignore
    
class OwnerCourseMixin(OwnerMixin):
    model= models.Course
    fields = ['subject', 'title', 'slug', 'overview']
    success_url = reverse_lazy('manage_course_list')

class OwnerCourseEditMixin(OwnerCourseMixin, OwnerEditMixin):
    template_name ='courses/manage/course/form.html'

class ManageCourseListView(OwnerCourseMixin, ListView):
    model = models.Course
    template_name = 'courses/manage/course/list.html'

class CourseCreateView(OwnerCourseEditMixin, CreateView):
    pass

class CourseUpdateView(OwnerCourseEditMixin, UpdateView):
    pass

class CourseDeleteView(OwnerCourseMixin, DeleteView):
    template_name = 'courses/manage/course/delete.html'



