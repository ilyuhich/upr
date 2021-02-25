# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.views.generic.base import TemplateView
from .models import *


class Morda(TemplateView):
    template_name = 'man/base.html'


class OpenProblems(ListView):
    model = Problem
    context_object_name = 'problems'

    def get_queryset(self):
        queryset = Problem.objects.filter(time_closed__isnull=True)
        return queryset


class AllProblems(ListView):
    model = Problem
    context_object_name = 'problems'


class DistrictList(ListView):
    model = District
    context_object_name = 'district_list'
    template_name = 'man/district_list.html'
    ordering = ['district_name']


class DistrictDetail(DetailView):
    model = District
    template_name = 'district_detail.html'


class DistrictCreate(CreateView):
    model = District
    fields = ['district_name']


class DistrictUpdate(UpdateView):
    model = District
    fields = '__all__'


class DistrictDelete(DeleteView):
    model = District
    success_url = reverse_lazy('district_list')


class ProblemCreate(CreateView):
    model = Problem
    fields = '__all__'


class ProblemDetail(DetailView):
    model = Problem
    context_object_name = 'problem'
    template_name = 'man/problem_detail.html'


class PlaceCreate(CreateView):
    model = Place
    fields = '__all__'