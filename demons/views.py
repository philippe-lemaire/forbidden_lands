from django.shortcuts import render
from django.http import HttpResponse
from demons.demon_generator import Demon


# Create your views here.


def create_demon(request):
    demon = Demon()
    context = {"demon": demon}
    return render(request, "demons/generate_demon.html", context=context)
