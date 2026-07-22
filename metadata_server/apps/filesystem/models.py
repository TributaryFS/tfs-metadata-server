import uuid

from django.db import models


class Directory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, null=False)
    owner = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="owned_directories"
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


class DirectorySubdirectoryAssociation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    parent_directory = models.ForeignKey(
        "filesystem.Directory",
        on_delete=models.CASCADE,
        related_name="child_associations",
    )
    child_directory = models.ForeignKey(
        "filesystem.Directory",
        on_delete=models.CASCADE,
        related_name="parent_associations",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "directory_subdirectory_associations"
        constraints = [
            models.UniqueConstraint(
                fields=["parent_directory", "child_directory"],
                name="uq_directory_hierarchy_parent_child",
            ),
        ]


class File(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, null=False)
    local_path = models.CharField(max_length=1024, null=False)
    tributary_path = models.CharField(max_length=1024, null=False)
    owner = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="owned_files"
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
        "users.User", on_delete=models.CASCADE, related_name="modified_files"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "files"


class DirectoryFileAssociation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    directory = models.ForeignKey(
        "filesystem.Directory",
        on_delete=models.CASCADE,
        related_name="file_associations",
    )
    file = models.ForeignKey(
        "filesystem.File",
        on_delete=models.CASCADE,
        related_name="directory_associations",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "directory_file_associations"
        constraints = [
            models.UniqueConstraint(
                fields=["directory", "file"],
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
        constraints = [
            models.UniqueConstraint(
                fields=["file", "chunk"],
                name="uq_file_chunk",
            ),
        ]
