import uuid
from django.db import models
from django.contrib.auth.models import User

class Rol(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=45, null=False, blank=False)
    description = models.CharField(max_length=250, null=False, blank=False)

    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, on_delete=models.RESTRICT, null=True, blank=True, related_name='rol_created_by')
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_by = models.ForeignKey(User, on_delete=models.RESTRICT, null=True, blank=True, related_name='rol_updated_by')
    updated_at = models.DateTimeField(auto_now=True)
