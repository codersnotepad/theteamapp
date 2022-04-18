from django.shortcuts import render
from . import forms
from . import models

# Create your views here.
def add(request):
    show_update_msg = False
    if request.POST:
        new_resource = forms.ResourceAddForm(request.POST)
        if new_resource.is_valid():
            resource_data = new_resource.save()
            show_update_msg = True

    resource_add_form = forms.ResourceAddForm()
    context = {
        "resource_add_form": resource_add_form,
        "form_media": resource_add_form.media,
        "show_update_msg": show_update_msg,
    }
    return render(request, "resource_add.html", context)


def view_all(request):
    most_recent = models.Fact.objects.all().order_by("-id")
    context = {
        "most_recent": most_recent,
    }
    return render(request, "resource_view_all.html", context)


def skills_by_skills_matrix(request):
    context = {
        'skills' : ['Python', 'R', 'Java', 'Power BI']
        ,'graph_data' : [
                        [3, 2, 2], 
                        [2, 1, -1], [3, 1, 1], 
                        [1, 0, 2],  [2, 0, 3],  [3, 0, 1],
                        ]
    }
    return render(request, "resource_skills_by_skills_matrix.html", context)