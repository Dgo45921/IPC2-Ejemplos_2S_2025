from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('saludo/', views.saludo),
    path('personas/', views.personas),
    path('personas/<int:pk>/', views.PersonaDetailView.as_view(), name='persona_detail'),
    ]