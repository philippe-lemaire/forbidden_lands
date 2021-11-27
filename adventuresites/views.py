from django.shortcuts import render
from django.http import HttpResponse
from .village_generator import Village


# Create your views here.


def generate_village(request):
    village = Village()
    context = {"village": village}
    return render(request, "adventuresites/generate_village.html", context=context)
