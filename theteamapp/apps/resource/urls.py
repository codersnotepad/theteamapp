from django.urls import path
from . import views

app_name = "rs"
urlpatterns = [
    path("add", views.add, name="add"),
    path("view_all", views.view_all, name="view_all"),
    path("skills_by_skills_matrix", views.skills_by_skills_matrix, name="skills_by_skills_matrix"),
]