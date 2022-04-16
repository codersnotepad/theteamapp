from django.shortcuts import render
from . import forms

# Create your views here.
def add_resource(request):
    add_resource_form = forms.AddResourceForm()
    context = {
        "add_resource_form": add_resource_form,
        "form_media": add_resource_form.media,
    }
    return render(request, "add_resource.html", context)