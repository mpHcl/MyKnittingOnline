from django.urls import path
from . import views

app_name = 'MyKnitting'

urlpatterns = [
    path("", views.index, name='index')
]
