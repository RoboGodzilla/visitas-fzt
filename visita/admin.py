from django.contrib import admin

from visita.models import Escuela, Profesor

# Register your models here.
@admin.register(Escuela)
class EscuelaAdmin(admin.ModelAdmin):

  pass
@admin.register(Profesor)
class ProfesorAdmin(admin.ModelAdmin):
  pass