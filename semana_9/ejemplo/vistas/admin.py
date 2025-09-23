from django.contrib import admin
from .models import Persona, Direccion



class DireccionInline(admin.TabularInline):
    model = Direccion
    extra = 1

@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    inlines = [DireccionInline]