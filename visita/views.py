from django.shortcuts import render
from django.contrib import messages

from visita.models import *
from .forms import *

# Create your views here.
def home(request, *args, **kwargs):
  return render(request, "home.html", {})

def tablavisita(request, *args, **kwargs):
  data = list(Visita.objects.values())
  campos = ["Nombre", "Activo"]
  contexto = {
    "data": data,
    "campos": campos,
    "registro": "registro",
    "menu": "visita",
    "submenu": "visita"
  }
  return render(request, "tabla.html", contexto)

def registrovisita(request, *args, **kwargs):
  if request.method == "POST":
    eform = VisitaEscuelaForm(request.POST)
    pform = VisitaProfesorForm(request.POST)
    form = VisitaForm(request.POST)
    print(form.data)
    print(form.errors)
    if form.is_valid():
      form.save()
      messages.success(request, "Visita registrada correctamente")
    else:
      form.add_error(None, "Visita no registrada")
  else:
    eform = VisitaEscuelaForm()
    pform = VisitaProfesorForm()
    form = VisitaForm()
  contexto = {
    "eform": eform,
    "pform": pform,
    "form": form,
    "menu": "visita",
    "submenu": "registro"
  }
  return render(request, "registro.html", contexto)

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

def registroescuela(request, *args, **kwargs):
  if request.method == "POST":
    form = EscuelaForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, "Escuela registrada correctamente")
    else:
      form.add_error(None, "Escuela no registrada")
  else:
    form = EscuelaForm()
  contexto = {
    "form": form,
    "menu": "datosvisita",
    "submenu": "escuela"
  }
  return render(request, "registro.html", contexto)

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

def registroprofesor(request, *args, **kwargs):
  if request.method == "POST":

    form = ProfesorForm(request.POST)

    if form.is_valid():
      form.save()
      messages.success(request, "Profesor registrado correctamente")
    else:
      form.add_error(None, "Profesor no registrado")
  else:
    form = ProfesorForm()
  contexto = {
    "form": form,
    "menu": "datosvisita",
    "submenu": "profesor"
  }
  return render(request, "registro.html", contexto)

def tablaasesor(request, *args, **kwargs):
  data = list(Asesoria.objects.values('nombre', 'area', 'is_active'))
  campos = ["Nombre", "Area de Asesoría", "Activo"]
  contexto = {
    "data": data,
    "campos": campos,
    "registro": "regasesor",
    "menu": "datosvisita",
    "submenu": "asesor"
  }
  return render(request, "tabla.html", contexto)

def registroasesor(request, *args, **kwargs):
  if request.method == "POST":
    form = AsesorForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, "Asesor registrado correctamente")
    else:
      form.add_error(None, "Asesor no registrado")
  else:
    form = AsesorForm()
  contexto = {
    "form": form,
    "menu": "datosvisita",
    "submenu": "asesor"
  }
  return render(request, "registro.html", contexto)