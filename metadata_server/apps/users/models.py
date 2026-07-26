from uuid import uuid4

from apps.filesystem.models import Directory
from django.db import models


class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    username = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "users"
        constraints = [
            models.UniqueConstraint(fields=["username"], name="uq_user_username"),
        ]

    @property
    def root_directory(self):
        return Directory.objects.get(owner=self, parent_directory=None)
