from uuid import uuid4

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
