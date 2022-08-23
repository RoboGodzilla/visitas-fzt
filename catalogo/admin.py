from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Pais)
class PaisAdmin(admin.ModelAdmin):
  pass

@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
  pass

@admin.register(Ciudad)
class CiudadAdmin(admin.ModelAdmin):
  pass