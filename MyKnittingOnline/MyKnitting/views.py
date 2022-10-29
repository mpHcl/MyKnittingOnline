from django.shortcuts import render

from django.contrib.auth.models import User
from .models import *
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, logout, login
from django.http import Http404, HttpResponse, FileResponse

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        projects = Project.objects.filter(owner=request.user)
        return render(request, 'MyKnitting/index.html', context={
            'projects' : projects, 
        })
    else:
        return HttpResponse("User not logged")


def projects(request): 
    if request.user.is_authenticated:
        projects = Project.objects.filter(owner=request.user)
        photos = {}
        for project in projects:
            photos_for_project = Photo.objects.filter(project=project)
            photos[project] = photos_for_project

        return render(request, 'MyKnitting/list/projects.html', context={
            'projects' : projects, 
            'photos' : photos,
        })
    else:
        return HttpResponse("User not logged")

def needles(request):
    if request.user.is_authenticated:
        needles = Needles.objects.filter(owner=request.user)
        return render(request, 'MyKnitting/list/needles.html', context={
            'needles' : needles, 
        })
    else:
        return HttpResponse("User not logged")

def yarns(request): 
    if request.user.is_authenticated:
        yarns = Yarn.objects.filter(owner=request.user)
        return render(request, 'MyKnitting/list/yarns.html', context={
            'yarns' : yarns, 
        })
    else:
        return HttpResponse("User not logged")