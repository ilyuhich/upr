from django.forms import ModelForm

from man.models import District, Problem


class DistrictForm(ModelForm):
    model = District
    fields = ['district_name']


class ProblemForm(ModelForm):
    model = Problem
    fields = '__all__'
