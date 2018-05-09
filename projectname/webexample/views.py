from django.shortcuts import render

# Create your views here.

from django.http import HttpResponce

def index(request):
    return HttpResponce("<h2>Назва розділу</h2>")
