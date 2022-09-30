import uuid
from django.db import models
from django.contrib.auth.models import User, Group, Permission
from django.contrib.postgres.fields import ArrayField


class Pais(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=50, null=False, blank=False, unique=True,error_messages={'unique':"Este pais ya ha sido registrado"})

    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, on_delete=models.RESTRICT, null=True, blank=True, related_name='pais_created_by')
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_by = models.ForeignKey(User, on_delete=models.RESTRICT, null=True, blank=True, related_name='pais_updated_by')
    updated_at = models.DateTimeField(auto_now=True)


class Estado(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)

    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, on_delete=models.RESTRICT, null=True, blank=True, related_name='estado_created_by')
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_by = models.ForeignKey(User, on_delete=models.RESTRICT, null=True, blank=True, related_name='estado_updated_by')
    updated_at = models.DateTimeField(auto_now=True)


class Ciudad(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)

    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, on_delete=models.RESTRICT, null=True, blank=True, related_name='ciudad_created_by')
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_by = models.ForeignKey(User, on_delete=models.RESTRICT, null=True, blank=True, related_name='ciudad_updated_by')
    updated_at = models.DateTimeField(auto_now=True)


class AreaAsesoria(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=50, null=False, blank=False)

    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, on_delete=models.RESTRICT, null=True, blank=True, related_name='areaase_created_by')
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_by = models.ForeignKey(User, on_delete=models.RESTRICT, null=True, blank=True, related_name='areaase_updated_by')
    updated_at = models.DateTimeField(auto_now=True)


class TipoVisita (models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=50, null=False, blank=False)

    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, on_delete=models.RESTRICT, null=True, blank=True, related_name='tipovis_created_by')
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_by = models.ForeignKey(User, on_delete=models.RESTRICT, null=True, blank=True, related_name='tipovis_updated_by')
    updated_at = models.DateTimeField(auto_now=True)


class Enfoque(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    tipo_visita = models.ForeignKey(TipoVisita, on_delete=models.CASCADE)
    valores = ArrayField(base_field=models.CharField(max_length=50), null=True, blank=True)

    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, on_delete=models.RESTRICT, null=True, blank=True, related_name='enfoque_created_by')
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_by = models.ForeignKey(User, on_delete=models.RESTRICT, null=True, blank=True, related_name='enfoque_updated_by')
    updated_at = models.DateTimeField(auto_now=True)