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
                fields=["name", "parent_directory"],
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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "files"
        constraints = [  # noqa: RUF012
            models.UniqueConstraint(
                fields=["name", "parent_directory"],
                name="uq_directory_file",
            ),
        ]


class FileVersion(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    file = models.ForeignKey(
        "filesystem.File",
        on_delete=models.CASCADE,
        related_name="versions",
    )
    checksum = models.CharField(max_length=255, null=False)
    size = models.BigIntegerField(null=False)
    version = models.IntegerField(null=False, default=1)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.RESTRICT,
        related_name="created_file_versions",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "file_versions"
        constraints = [  # noqa: RUF012
            models.UniqueConstraint(
                fields=["file", "version"],
                name="uq_file_version",
            ),
        ]


class FileChunkAssociation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    file_version = models.ForeignKey(
        "filesystem.FileVersion",
        on_delete=models.CASCADE,
        related_name="chunk_associations",
    )
    chunk = models.ForeignKey(
        "storage.Chunk",
        on_delete=models.CASCADE,
        related_name="file_associations",
    )
    logical_offset = models.BigIntegerField(null=False)
    chunk_index = models.IntegerField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "file_chunk_associations"
        constraints = [  # noqa: RUF012
            models.UniqueConstraint(
                fields=["file_version", "chunk"],
                name="uq_file_chunk",
            ),
            models.UniqueConstraint(
                fields=["file_version", "logical_offset"],
                name="uq_file_version_offset",
            ),
            models.UniqueConstraint(
                fields=["file_version", "chunk_index"],
                name="uq_file_version_chunk_index",
            ),
        ]
