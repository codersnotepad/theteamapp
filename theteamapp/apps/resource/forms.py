from django import forms
from . import models

class AddResourceForm(forms.ModelForm):
    class Meta:
        fields = ['name',
            'role',
            'python',
            'r',
            'java',
            'powerbi',
        ]
        model = models.Resource_Fact