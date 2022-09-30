from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from collections import defaultdict

from catalogo.models import *

from .forms import *

# Create your views here.
@login_required
def home(request, *args, **kwargs):
  return render(request, "home.html", {})

@login_required
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

@login_required
def registropais(request, *args, **kwargs):
  if request.method == "POST":
    form = PaisForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, "Pais registrado correctamente")
    else:
      messages.error(request, "Pais no registrado")
  else:
    form = PaisForm()
  contexto = {
    "form": form,
    "menu": "catalogo",
    "submenu": "pais"
  }
  return render(request, "registro.html", contexto)

@login_required
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

@login_required
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

@login_required
def registroestado(request, *args, **kwargs):
  if request.method == "POST":
    form = EstadoForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, "Estado registrado correctamente")
    else:
      messages.error(request, "Estado no registrado")
  else:
    form = EstadoForm()
  contexto = {
    "form": form,
    "menu": "catalogo",
    "submenu": "estado"
  }
  return render(request, "registro.html", contexto)

@login_required
def tablaciudad(request, *args, **kwargs):
  data = list(Ciudad.objects.values('nombre', 'estado'))
  for d in data:
    d['pais'] = Estado.objects.get(id=d['estado']).pais.nombre
    d['is_active'] = Estado.objects.get(id=d['estado']).is_active
    d['estado'] = Estado.objects.get(id=d['estado']).nombre
  campos = ["Nombre", "Estado", "Pais", "Activo"]
  contexto = {
    "data": data,
    "campos": campos,
    "registro": "regciudad",
    "menu": "catalogo",
    "submenu": "ciudad"
  }
  return render(request, "tabla.html", contexto)

@login_required
def registrociudad(request, *args, **kwargs):
  if request.method == "POST":
    form = CiudadForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, "Ciudad registrada correctamente")
    else:
      messages.error(request, "Ciudad no registrada")
  else:
    form = CiudadForm()
  contexto = {
    "form": form,
    "menu": "catalogo",
    "submenu": "ciudad"
  }
  return render(request, "registro.html", contexto)

@login_required
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

@login_required
def registroareaasesoria(request, *args, **kwargs):
  if request.method == "POST":
    form = AreaAsesoriaForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, "Area de asesoria registrada correctamente")
    else:
      messages.error(request, "Area de asesoria no registrada")
  else:
    form = AreaAsesoriaForm()
  contexto = {
    "form": form,
    "menu": "datosvisita",
    "submenu": "areaasesor"
  }
  return render(request, "registro.html", contexto)

@login_required
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

@login_required
def registrotipovisita(request, *args, **kwargs):
  if request.method == "POST":
    form = TipoVisitaForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, "Tipo de visita registrada correctamente")
    else:
      messages.error(request, "Tipo de visita no registrada")
  else:
    form = TipoVisitaForm()
  contexto = {
    "form": form,
    "menu": "datosvisita",
    "submenu": "tipovisita"
  }
  return render(request, "registro.html", contexto)

@login_required
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

@login_required
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
      messages.error(request, "Enfoque no registrado")
  else:
    form = EnfoqueForm()
  contexto = {
    "form": form,
    "menu": "datosvisita",
    "submenu": "enfoque"
  }
  return render(request, "registro.html", contexto)

def tablausuarios(request, *args, **kwargs):
  data = list(User.objects.values('username', 'first_name', 'last_name', 'groups', 'is_active'))
  campos = ["Usuario", "Nombre", "Apellido", "Roles", "Activo"]
  contexto = {
    "data": data,
    "campos": campos,
    "registro": "regusuario",
    "menu": "cuentas",
    "submenu": "usuarios"
  }
  return render(request, "tabla.html", contexto)

def registrousuario(request, *args, **kwargs):
  if request.method == "POST":
    form = UserForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, "Usuario registrado correctamente")
    else:
      messages.error(request, "Usuario no registrado")
  else:
    form = UserForm()
  contexto = {
    "form": form,
    "menu": "cuentas",
    "submenu": "usuarios"
  }
  return render(request, "registro.html", contexto)

def tablaroles(request, *args, **kwargs):
  queryset = Group.objects.values('id', 'name')
  for q in queryset:
    q['permissions'] = Group.objects.get(pk = q['id']).permissions.values()

  data = list(queryset)
  # newdata = defaultdict(list)
  # for d in data:
  #   d['permissions'] = Permission.objects.get(id=d['permissions']).name
  print(data)
  campos = ["Nombre", "Permisos"]
  contexto = {
    "data": data,
    "campos": campos,
    "registro": "regrol",
    "menu": "cuentas",
    "submenu": "roles"
  }
  return render(request, "tabla.html", contexto)

def registrorol(request, *args, **kwargs):
  if request.method == "POST":
    form = GroupForm(request.POST)
    if form.is_valid():
      # form.save()
      print(form.cleaned_data)
      messages.success(request, "Rol registrado correctamente")
    else:
      messages.error(request, "Rol no registrado")
  else:
    form = GroupForm()
  contexto = {
    "form": form,
    "menu": "cuentas",
    "submenu": "roles"
  }
  return render(request, "registro.html", contexto)