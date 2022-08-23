from django.shortcuts import render
from django.contrib import messages

from catalogo.models import *

from .forms import *

# Create your views here.
def home(request, *args, **kwargs):
  return render(request, "home.html", {})

def tablapais(request, *args, **kwargs):
  data = list(Pais.objects.values('id', 'nombre', 'is_active'))
  campos = ["Nombre", "Activo"]
  contexto = {
    "data": data,
    "campos": campos,
    "registro": "regpais",
    "detalles": "detpais",
    "menu": "catalogo",
    "submenu": "pais"
  }
  return render(request, "tabla.html", contexto)

def registropais(request, *args, **kwargs):
  if request.method == "POST":
    form = PaisForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, "Pais registrado correctamente")
    else:
      form.add_error(None, "Pais no registrado")
  else:
    form = PaisForm()
  contexto = {
    "form": form,
    "menu": "catalogo",
    "submenu": "pais"
  }
  return render(request, "registro.html", contexto)

def detallepais(request, id, *args, **kwargs):
  try:
    pais = Pais.objects.get(id=id)
  except Pais.DoesNotExist:
    messages.error(request, "Pais no existe")
    return render(request, "home.html", {})
  contexto = {
    "data": pais,
    "menu": "catalogo",
    "submenu": "pais"
  }
  return render(request, "detalles.html", contexto)

def tablaestado(request, *args, **kwargs):
  data = list(Estado.objects.values('nombre', 'pais', 'is_active'))
  for d in data:
    d['pais'] = Pais.objects.get(id=d['pais']).nombre    
  campos = ["Nombre", "Pais", "Activo"]
  contexto = {
    "data": data,
    "campos": campos,
    "registro": "regestado",
    "menu": "catalogo",
    "submenu": "estado"
  }
  return render(request, "tabla.html", contexto)

def registroestado(request, *args, **kwargs):
  if request.method == "POST":
    form = EstadoForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, "Estado registrado correctamente")
    else:
      form.add_error(None, "Estado no registrado")
  else:
    form = EstadoForm()
  contexto = {
    "form": form,
    "menu": "catalogo",
    "submenu": "estado"
  }
  return render(request, "registro.html", contexto)

def tablaciudad(request, *args, **kwargs):
  data = list(Ciudad.objects.values('nombre', 'estado', 'is_active'))
  for d in data:
    d['estado'] = Estado.objects.get(id=d['estado']).nombre
  campos = ["Nombre", "Estado", "Activo"]
  contexto = {
    "data": data,
    "campos": campos,
    "registro": "regciudad",
    "menu": "catalogo",
    "submenu": "ciudad"
  }
  return render(request, "tabla.html", contexto)

def registrociudad(request, *args, **kwargs):
  if request.method == "POST":
    form = CiudadForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, "Ciudad registrada correctamente")
    else:
      form.add_error(None, "Ciudad no registrada")
  else:
    form = CiudadForm()
  contexto = {
    "form": form,
    "menu": "catalogo",
    "submenu": "ciudad"
  }
  return render(request, "registro.html", contexto)

def tablaareaasesoria(request, *args, **kwargs):
  data = list(AreaAsesoria.objects.values('nombre', 'is_active'))
  campos = ["Nombre", "Activo"]
  contexto = {
    "data": data,
    "campos": campos,
    "registro": "regareaasesoria",
    "menu": "datosvisita",
    "submenu": "areaasesor"
  }
  return render(request, "tabla.html", contexto)

def registroareaasesoria(request, *args, **kwargs):
  if request.method == "POST":
    form = AreaAsesoriaForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, "Area de asesoria registrada correctamente")
    else:
      form.add_error(None, "Area de asesoria no registrada")
  else:
    form = AreaAsesoriaForm()
  contexto = {
    "form": form,
    "menu": "datosvisita",
    "submenu": "areaasesor"
  }
  return render(request, "registro.html", contexto)

def tablatipovisita(request, *args, **kwargs):
  data = list(TipoVisita.objects.values('nombre', 'is_active'))
  campos = ["Nombre", "Activo"]
  contexto = {
    "data": data,
    "campos": campos,
    "registro": "regtipovisita",
    "menu": "datosvisita",
    "submenu": "tipovisita"
  }
  return render(request, "tabla.html", contexto)

def registrotipovisita(request, *args, **kwargs):
  if request.method == "POST":
    form = TipoVisitaForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, "Tipo de visita registrada correctamente")
    else:
      form.add_error(None, "Tipo de visita no registrada")
  else:
    form = TipoVisitaForm()
  contexto = {
    "form": form,
    "menu": "datosvisita",
    "submenu": "tipovisita"
  }
  return render(request, "registro.html", contexto)

def tablaenfoque(request, *args, **kwargs):
  data = list(Enfoque.objects.values('nombre', 'tipo_visita', 'is_active'))
  for d in data:
    d['tipo_visita'] = TipoVisita.objects.get(id=d['tipo_visita']).nombre
  campos = ["Nombre", "Tipo Visita", "Activo"]
  contexto = {
    "data": data,
    "campos": campos,
    "registro": "regenfoque",
    "menu": "datosvisita",
    "submenu": "enfoque"
  }
  return render(request, "tabla.html", contexto)

def registroenfoque(request, *args, **kwargs):
  if request.method == "POST":
    form = EnfoqueForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, "Enfoque registrado correctamente")
      # from django.db import IntegrityError

      # except IntegrityError as e: 
      #   if 'unique constraint' in e.message:
      #     pass
    else:
      form.add_error(None, "Enfoque no registrado")
  else:
    form = EnfoqueForm()
  contexto = {
    "form": form,
    "menu": "datosvisita",
    "submenu": "enfoque"
  }
  return render(request, "registro.html", contexto)