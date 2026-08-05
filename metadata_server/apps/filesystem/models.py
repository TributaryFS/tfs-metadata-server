import uuid

from django.conf import settings
from django.db import models


class Directory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, null=False)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.RESTRICT,
        related_name="owned_directories",
    )
    parent_directory = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="subdirectories",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "directories"
        constraints = [  # noqa: RUF012
            models.UniqueConstraint(
                fields=["name", "owner", "parent_directory"],
                name="uq_directory_hierarchy_parent_child",
            ),
        ]


class File(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, null=False)
    local_path = models.CharField(max_length=1024, null=False)
    tributary_path = models.CharField(max_length=1024, null=False)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.RESTRICT, related_name="owned_files"
    )
    parent_directory = models.ForeignKey(
        "filesystem.Directory", on_delete=models.CASCADE, related_name="files"
    )
    checksum = models.CharField(max_length=255, null=False)
    size = models.BigIntegerField(null=False)
    version = models.IntegerField(null=False, default=1)
    prev_version_file_id = models.ForeignKey(
        "self", on_delete=models.SET_NULL, null=True, blank=True
    )
    last_modified = models.DateTimeField(auto_now=True)
    last_modified_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="modified_files",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "files"
        constraints = [  # noqa: RUF012
            models.UniqueConstraint(
                fields=["name", "owner", "parent_directory"],
                name="uq_directory_file",
            ),
        ]


class FileChunkAssociation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    file = models.ForeignKey(
        "filesystem.File",
        on_delete=models.CASCADE,
        related_name="chunk_associations",
    )
    chunk = models.ForeignKey(
        "storage.Chunk",
        on_delete=models.CASCADE,
        related_name="file_associations",
    )
    chunk_index = models.IntegerField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "file_chunk_associations"
        constraints = [  # noqa: RUF012
            models.UniqueConstraint(
                fields=["file", "chunk"],
                name="uq_file_chunk",
            ),
        ]
