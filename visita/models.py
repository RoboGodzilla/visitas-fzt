import uuid
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User

from catalogo.models import AreaAsesoria, Ciudad, Enfoque, TipoVisita

# Create your models here.
class Escuela(models.Model):
    MODALIDADES = [( 'Regular','Regular' ), ( 'Multigrado','Multigrado' )]
    DEPENDENCIAS = [( 'Pública','Pública' ), ( 'Subvencionada','Subvencionada' )]

    codigo = models.DecimalField(primary_key=True, null=False, blank=False, max_digits=5, decimal_places=0)
    nombre = models.CharField(max_length=50)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    modalidad = models.CharField(max_length=50, choices=MODALIDADES, default='Regular')
    dependencia = models.CharField(max_length=50, choices=DEPENDENCIAS, default='Pública')

    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, on_delete=models.RESTRICT, null=True, blank=True, related_name='escuela_created_by')
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_by = models.ForeignKey(User, on_delete=models.RESTRICT, null=True, blank=True, related_name='escuela_updated_by')
    updated_at = models.DateTimeField(auto_now=True)

class Profesor(models.Model):
    GRADOS = [( 1,'1ro' ), ( 2,'2do' ), ( 3,'3ro' ), ( 4,'4to' ), ( 5,'5to' ), ( 6,'6to' ), ( 7,'7mo' ), ( 8,'8vo' ), ( 9,'9no' ), ( 10,'10mo' ), ( 11,'11mo')]

    codigo = models.AutoField(primary_key=True, editable=False)
    nombre = models.CharField(max_length=100)
    cedula = models.CharField(max_length=14)
    edad = models.PositiveIntegerField(blank=True, null=True)
    telefono = models.PositiveIntegerField(blank=True, null=True)
    grados_asign = ArrayField(base_field=models.IntegerField(choices=GRADOS))
    escuela = models.ForeignKey(Escuela, on_delete=models.CASCADE)

    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, on_delete=models.RESTRICT, null=True, blank=True, related_name='profesor_created_by')
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_by = models.ForeignKey(User, on_delete=models.RESTRICT, null=True, blank=True, related_name='profesor_updated_by')
    updated_at = models.DateTimeField(auto_now=True)

class Asesoria(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=50)
    area = models.ForeignKey(AreaAsesoria, on_delete=models.CASCADE)

    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, on_delete=models.RESTRICT, null=True, blank=True, related_name='asesoria_created_by')
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_by = models.ForeignKey(User, on_delete=models.RESTRICT, null=True, blank=True, related_name='asesoria_updated_by')
    updated_at = models.DateTimeField(auto_now=True)

class Visita(models.Model):
    MODALIDAD = [( 'Presencial','Presencial' ), ( 'Remota','Remota' )]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fecha = models.DateField()
    duracion = models.DurationField()
    profesor = models.ManyToManyField(Profesor, through='DetalleProfesor')
    asesoria = models.ForeignKey(Asesoria, on_delete=models.CASCADE)
    tipo_visita = models.ForeignKey(TipoVisita, on_delete=models.CASCADE)
    modalidad_visita = models.CharField(max_length=50, choices=MODALIDAD, default='Presencial')
    comentarios = models.CharField(max_length=200)

    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, on_delete=models.RESTRICT, null=True, blank=True, related_name='visita_created_by')
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_by = models.ForeignKey(User, on_delete=models.RESTRICT, null=True, blank=True, related_name='visita_updated_by')
    updated_at = models.DateTimeField(auto_now=True)

class DetalleProfesor(models.Model):
    visita = models.ForeignKey(Visita, on_delete=models.CASCADE)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    enfoque = models.ManyToManyField(Enfoque)

    created_by = models.ForeignKey(User, on_delete=models.RESTRICT, null=True, blank=True, related_name='detalle_enfoques_created_by')
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_by = models.ForeignKey(User, on_delete=models.RESTRICT, null=True, blank=True, related_name='detalle_enfoques_updated_by')
    updated_at = models.DateTimeField(auto_now=True)