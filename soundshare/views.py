from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("SoundShare - The Web App to Share and Rate Music!")

# Create your views here.
