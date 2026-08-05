from uuid import uuid4

from apps.filesystem.models import Directory
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "users"

    @property
    def root_directory(self):
        return Directory.objects.get(owner=self, parent_directory=None)
