from statistics import mode
from turtle import color, title
from django.db import models
from django.contrib.auth.models import User


# Project model will contain data like photos of project, pattern used, if it was completed or not, 
class Project(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    completed = models.BooleanField()

    # To implement in future (something like social media thing)
    public = models.BooleanField()


# This will make available to add more than one photo to one project 
class Photo(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    photo = models.FileField(upload_to="project_photos")


class Pattern(models.Model): 
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    pattern = models.FileField(upload_to="project_pattern")


# Model contianing information about yarn
class Yarn(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    color_code = models.CharField(max_length=7)
    amount_owned = models.IntegerField()
    size = models.IntegerField()
    material = models.CharField(max_length=50)


# This will make available to add more than one yarn to project, and yarn to more than one project 
class YarnsForProject(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    yarn = models.ForeignKey(Yarn, on_delete=models.CASCADE)
    amount_needed = models.IntegerField()


# Model contianing information about needles
class Needles(models.Model): 
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    size = models.IntegerField()
    length = models.IntegerField()


# This will make available to add more than one needles to project, and needles to more than one project 
class NeedlesForProject(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    needles = models.ForeignKey(Needles, on_delete=models.CASCADE)