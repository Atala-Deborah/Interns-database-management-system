from django import forms
from .models import Intern
from .models import Workshop
from .models import Project

class InternForm(forms.ModelForm):
    class Meta:
        model = Intern
        fields = '__all__'

class WorkshopForm(forms.ModelForm):
    class Meta:
        model = Workshop
        fields = ['title', 'date', 'time', 'location', 'description', 'image']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }

from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        widgets = {
            'status': forms.Select(choices=Project.STATUS_CHOICES)
        }
