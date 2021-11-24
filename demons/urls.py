from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = "demons"

urlpatterns = [
    path("", TemplateView.as_view(template_name="demons/index.html"), name="index"),
    path("generate_demon/", views.create_demon, name="generate_demon"),
]
