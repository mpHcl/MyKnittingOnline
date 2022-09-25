from django.urls import path
from . import views

app_name = 'MyKnitting'

urlpatterns = [
    path("", views.index, name='index'),
    path("yarns", views.yarns, name='yarns_list'),
    path("needles", views.needles, name='needles_list'),
    path("projects", views.projects, name='projects_list')
]