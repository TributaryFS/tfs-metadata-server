from uuid import uuid4

from django.db import models

from permissioins.choices import Permission


class DirectoryPermission(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    directory = models.ForeignKey(
        "filesystem.Directory", on_delete=models.CASCADE, related_name="permissions"
    )
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="directory_permissions"
    )
    permission_level = models.CharField(
        max_length=50, choices=Permission.choices, default=Permission.READ
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "directory_permissions"
        constraints = [
            models.UniqueConstraint(
                fields=["directory", "user"], name="uq_directory_permission"
            ),
        ]


class FilePermission(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    file = models.ForeignKey(
        "filesystem.File", on_delete=models.CASCADE, related_name="permissions"
    )
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="file_permissions"
    )
    permission_level = models.CharField(
        max_length=50, choices=Permission.choices, default=Permission.READ
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "file_permissions"
        constraints = [
            models.UniqueConstraint(fields=["file", "user"], name="uq_file_permission"),
        ]
