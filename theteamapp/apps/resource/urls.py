from django.urls import path
from . import views

app_name = "rs"
urlpatterns = [
    path("add", views.add_resource, name="add_resource"),
]