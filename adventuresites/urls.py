from django.urls import path
from . import views


app_name = "adventuresites"

urlpatterns = [
    path("generate_village/", views.generate_village, name="generate_village"),
]
