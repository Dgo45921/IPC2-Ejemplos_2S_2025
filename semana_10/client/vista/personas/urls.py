from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('crearPersona', views.crear),
    path('nuevaMascota', views.nueva_mascota),
]