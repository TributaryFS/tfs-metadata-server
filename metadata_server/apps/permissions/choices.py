from django.db import models


class Permission(models.TextChoices):
    READ = "read", "Read Only"
    WRITE = "write", "Read & Write"
    OWNER = "owner", "Owner"
    ORPHAN = "orphan", "Orphan"
