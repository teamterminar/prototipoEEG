from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('/entrena', views.entrena, name='entrena'),
    path('/clasifica', views.clasifica, name='clasifica'),


]