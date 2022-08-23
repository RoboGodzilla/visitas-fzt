import imp
from django import forms
import django.contrib.postgres.forms as pgforms

from .models import *

class NombreModelChoiceField(forms.ModelChoiceField):
  def label_from_instance(self, obj):
    return obj.nombre

class MatCheckboxInput(forms.CheckboxInput):
    template_name = 'matcheckbox.html'

class PaisForm(forms.ModelForm):

  is_active = MatCheckboxInput()

  class Meta:
    model = Pais
    fields = [
      'nombre',
      # 'is_active',
    ]

    widgets = {
      'nombre': forms.TextInput(attrs={'class': 'validate'}),	
      # 'is_active': MatCheckboxInput(attrs={'label': 'Is Active', 'class': 'filled-in'}),
    }
    # labels = {
    #   'nombre': 'Nombre',
    #   'is_active': '',
    # }

class EstadoForm(forms.ModelForm):
  pais = NombreModelChoiceField(queryset=Pais.objects.filter(is_active=True))
  class Meta:
    model = Estado
    fields = [
      'nombre',
      'pais',
    ]

class CiudadForm(forms.ModelForm):
  estado = NombreModelChoiceField(queryset=Estado.objects.filter(is_active=True))
  class Meta:
    model = Ciudad
    fields = [
      'nombre',
      'estado',
    ]

AreaAsesoriaForm = forms.modelform_factory(AreaAsesoria, fields=['nombre'])

TipoVisitaForm = forms.modelform_factory(TipoVisita, fields=['nombre'])

class EnfoqueForm(forms.ModelForm):
  nombre = forms.CharField(max_length=100, label='Nombre')
  tipo_visita = NombreModelChoiceField(queryset=TipoVisita.objects.filter(is_active=True))
  valores = pgforms.SimpleArrayField(forms.CharField(max_length=100), label='Valores', required=False)
  
  class Meta:
    model = Enfoque
    fields = [
      'nombre',
      'tipo_visita',
      'valores',
    ]
