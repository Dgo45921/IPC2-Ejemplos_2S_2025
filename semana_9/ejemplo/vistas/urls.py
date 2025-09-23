from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('saludo/', views.saludo),
    path('personas/', views.personas),
    ]