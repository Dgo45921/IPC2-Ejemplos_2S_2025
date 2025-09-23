from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('lista_alumnos/', views.lista_alumnos),
    ]