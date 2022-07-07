from django.http import HttpResponse
from django.shortcuts import render
import h11

# Create your views here.


def index(request):
    return HttpResponse("This works!")
