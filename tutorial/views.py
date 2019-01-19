from django.shortcuts import render
from django.views.generic import ( View, TemplateView,
                                    ListView, DetailView,
                                    CreateView, UpdateView,
                                    DeleteView )
from django.http import HttpResponse
from .models import *
from django.urls import reverse_lazy

class IndexView(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = 'Basic Injecttion'
        return context

class SchoolListView(ListView):
    context_object_name = 'schools'
    model = School

class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = School
    template_name = 'tutorial/school_detail.html'

class SchoolCreateView(CreateView):
    model = School
    fields = ('name', 'principal', 'location')

class SchoolUpdateView(UpdateView):
    fields = ('name', 'principal')
    model = School

class SchoolDeleteView(DeleteView):
    model = School
    success_url = reverse_lazy('tutorial:list')

class StudentDetailView(DetailView):
    # context_object_name = 'student_detail'
    model = Student
    # template_name = 'tutorial/student_detail.html'

class StudentCreateView(CreateView):
    model = Student
    fields = '__all__'

class StudentUpdateView(UpdateView):
    model = Student
    fields = ('age', 'school')

class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('tutorial:list')

class CBView(View):
    def get(self, request):
        return HttpResponse('Class Based Views are cool!!')
