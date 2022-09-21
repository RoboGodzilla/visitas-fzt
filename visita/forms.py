from django import forms
from django.conf import settings
import django.contrib.postgres.forms as pgforms

from .models import *

class IdNombreModelChoiceField(forms.ModelChoiceField):
  def label_from_instance(self, obj):
    label = str(obj.codigo) + " [" + obj.nombre + "]"
    return label

class IdNombreMultipleModelChoiceField(forms.ModelMultipleChoiceField):
  def label_from_instance(self, obj):
    label = str(obj.codigo) + " [" + obj.nombre + "]"
    return label

class NombreMultipleModelChoiceField(forms.ModelMultipleChoiceField):
  def label_from_instance(self, obj):
    label = obj.nombre
    return label

class NombreModelChoiceField(forms.ModelChoiceField):
  def label_from_instance(self, obj):
    label = obj.nombre
    return label

class VisitaEscuelaForm(forms.ModelForm):
  escuela = IdNombreModelChoiceField(queryset=Escuela.objects.filter(is_active=True))
  class Meta:
    model = Visita
    fields = [
      'escuela'
    ]

class DetalleProfesorForm(forms.ModelForm):
  profesor = NombreModelChoiceField(queryset=Profesor.objects.filter(is_active=True))
  enfoque = forms.ModelMultipleChoiceField(queryset=Enfoque.objects.filter(is_active=True), widget=forms.CheckboxSelectMultiple, required=True)
  class Meta:
    model = DetalleProfesor
    exclude = [
      'is_active',
      'created_by',
      'created_at',
      'updated_by',
      'updated_at',
    ]

class VisitaForm(forms.ModelForm):
  escuela = forms.HiddenInput()
  asesoria = NombreModelChoiceField(queryset=Asesoria.objects.filter(is_active=True))
  tipo_visita = NombreModelChoiceField(queryset=TipoVisita.objects.filter(is_active=True))
  modalidad_visita = forms.ChoiceField(choices=Visita.MODALIDAD, required=True)
  fecha = forms.DateField(widget=forms.DateInput(attrs={'class': 'datepicker'}), input_formats=settings.DATE_INPUT_FORMATS)
  duracion = forms.DurationField(widget=forms.NumberInput(attrs={'class': 'validate'}))
  comentarios = forms.CharField(max_length=500, required=False)
  class Meta:
    model = Visita
    fields = [
      'escuela',
      'asesoria',
      'tipo_visita',
      'modalidad_visita',
      'fecha',
      'duracion',
      'comentarios',
    ]

class EscuelaForm(forms.ModelForm):
  ciudad = NombreModelChoiceField(queryset=Ciudad.objects.filter(is_active=True))
  class Meta:
    model = Escuela
    exclude = [
      'is_active',
      'created_by',
      'created_at',
      'updated_by',
      'updated_at',
    ]

class ProfesorForm(forms.ModelForm):
  grados_asign = pgforms.SimpleArrayField(
    base_field=forms.IntegerField(),
    widget = forms.SelectMultiple(choices=Profesor.GRADOS),
  )
  escuela = NombreModelChoiceField(queryset=Escuela.objects.filter(is_active=True))
  edad = forms.IntegerField( required=False )
  telefono = forms.IntegerField( required=False )
  class Meta:
    model = Profesor
    exclude = [
      'is_active',
      'created_by',
      'created_at',
      'updated_by',
      'updated_at',
    ]

class AsesorForm(forms.ModelForm):
  area = NombreModelChoiceField(queryset=AreaAsesoria.objects.filter(is_active=True))
  class Meta:
    model = Asesoria
    exclude = [
      'is_active',
      'created_by',
      'created_at',
      'updated_by',
      'updated_at',
    ]