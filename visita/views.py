from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from visita.models import *
from .forms import *

# Create your views here.
@login_required
def home(request, *args, **kwargs):
  return render(request, "home.html", {})

@login_required
def tablavisita(request, *args, **kwargs):
  data = list(Visita.objects.values(
    'id',
    'escuela_id',
    'asesoria_id',
    'tipo_visita_id',
    'modalidad_visita',
    'fecha',
    'duracion',
    'comentarios',
    ))
  for d in data:
    d['tipo_visita_id'] = TipoVisita.objects.get(id=d['tipo_visita_id']).nombre
    d['escuela_id'] = Escuela.objects.get(codigo=d['escuela_id']).nombre
    d['asesoria_id'] = Asesoria.objects.get(id=d['asesoria_id']).nombre
    d['profesores'] = list(DetalleProfesor.objects.filter(visita_id=d['id']).values())
    d['is_active'] = Visita.objects.get(id=d['id']).is_active
  campos = ["Escuela", "Asesor", "Tipo Visita", "Modalidad", "Fecha", "Duracion", "Comentarios", "Profesores", "Activo"]
  contexto = {
    "data": data,
    "campos": campos,
    "registro": "registro",
    "menu": "visita",
    "submenu": "visita"
  }
  return render(request, "tabla.html", contexto)

@login_required
def registrovisita(request, *args, **kwargs):

  DetalleProfesorFormSet = forms.inlineformset_factory(Visita, DetalleProfesor, form=DetalleProfesorForm, extra=2, can_delete=False)

  eform = VisitaEscuelaForm(request.POST or None)
  pform = DetalleProfesorFormSet(request.POST or None)
  form = VisitaForm(request.POST or None)

  if request.method == "POST":
    print(form.errors)
    if form.is_valid() and eform.is_valid() and pform.is_valid():
      print(form.cleaned_data)
      visita = Visita.objects.create(
        escuela=eform.cleaned_data['escuela'],
        asesoria=form.cleaned_data['asesoria'],
        tipo_visita=form.cleaned_data['tipo_visita'],
        modalidad_visita=form.cleaned_data['modalidad_visita'],
        fecha=form.cleaned_data['fecha'],
        duracion=form.cleaned_data['duracion'],
        comentarios=form.cleaned_data['comentarios'],
      )
      for p in pform.cleaned_data:
        if p:
          p.pop('visita')
          instancia = p.pop('enfoque')
          detalleprofesor = DetalleProfesor.objects.create(visita=visita, **p)
          detalleprofesor.enfoque.set(instancia)
      messages.success(request, "Visita registrada correctamente")
    else:
      messages.error(request, "Visita no registrada")

  contexto = {
    "eform": eform,
    "pform": pform,
    "form": form,
    "menu": "visita",
    "submenu": "registro"
  }
  return render(request, "registro.html", contexto)

@login_required
def tablaescuela(request, *args, **kwargs):
  data = list(Escuela.objects.values('codigo','nombre', 'ciudad', 'modalidad', 'dependencia', 'is_active'))
  for d in data:
    d['ciudad'] = Ciudad.objects.get(id=d['ciudad']).nombre
  campos = ["Codigo", "Nombre", "Ciudad", "Modalidad", "Dependencia", "Activo"]
  contexto = {
    "data": data,
    "campos": campos,
    "registro": "regescuela",
    "menu": "datosvisita",
    "submenu": "escuela"
  }
  return render(request, "tabla.html", contexto)

@login_required
def registroescuela(request, *args, **kwargs):
  if request.method == "POST":
    form = EscuelaForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, "Escuela registrada correctamente")
    else:
      messages.error(request, "Escuela no registrada")
  else:
    form = EscuelaForm()
  contexto = {
    "form": form,
    "menu": "datosvisita",
    "submenu": "escuela"
  }
  return render(request, "registro.html", contexto)

@login_required
def tablaprofesor(request, *args, **kwargs):
  data = list(Profesor.objects.values('codigo', 'nombre', 'grados_asign', 'escuela', 'is_active'))
  for d in data:
    d['escuela'] = Escuela.objects.get(codigo=d['escuela']).nombre
  campos = ["Codigo", "Nombre", "Grados Asignados", "Escuela", "Activo"]
  contexto = {
    "data": data,
    "campos": campos,
    "registro": "regprofesor",
    "menu": "datosvisita",
    "submenu": "profesor"
  }
  return render(request, "tabla.html", contexto)

@login_required
def registroprofesor(request, *args, **kwargs):
  if request.method == "POST":

    form = ProfesorForm(request.POST)

    if form.is_valid():
      form.save()
      messages.success(request, "Profesor registrado correctamente")
    else:
      messages.error(request, "Profesor no registrado")
  else:
    form = ProfesorForm()
  contexto = {
    "form": form,
    "menu": "datosvisita",
    "submenu": "profesor"
  }
  return render(request, "registro.html", contexto)

@login_required
def tablaasesor(request, *args, **kwargs):
  data = list(Asesoria.objects.values('nombre', 'area', 'is_active'))
  for d in data:
    d['area'] = AreaAsesoria.objects.get(id=d['area']).nombre
  campos = ["Nombre", "Area de Asesoría", "Activo"]
  contexto = {
    "data": data,
    "campos": campos,
    "registro": "regasesor",
    "menu": "datosvisita",
    "submenu": "asesor"
  }
  return render(request, "tabla.html", contexto)

@login_required
def registroasesor(request, *args, **kwargs):
  if request.method == "POST":
    form = AsesorForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, "Asesor registrado correctamente")
    else:
      messages.error(request, "Asesor no registrado")
  else:
    form = AsesorForm()
  contexto = {
    "form": form,
    "menu": "datosvisita",
    "submenu": "asesor"
  }
  return render(request, "registro.html", contexto)