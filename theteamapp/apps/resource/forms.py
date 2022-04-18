from django import forms
from . import models

class ResourceAddForm(forms.ModelForm):
    class Meta:
        fields = ['name',
            'employee_id',
            'role',
            'python',
            'r',
            'java',
            'powerbi',
        ]
        model = models.Fact