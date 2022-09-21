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