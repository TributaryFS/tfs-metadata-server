import uuid

from apps.uploads.choices import UploadStatus
from django.db import models


class Upload(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    status = models.CharField(
        max_length=50, choices=UploadStatus.choices, default=UploadStatus.Initiated
    )
    started_at = models.DateTimeField(null=True)
    completed_at = models.DateTimeField(null=True)
    total_files = models.IntegerField(null=False)
    expires_at = models.DateTimeField(null=True)
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="uploads"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "uploads"


class UploadFile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    upload = models.ForeignKey(
        "uploads.Upload", on_delete=models.CASCADE, related_name="files"
    )
    file = models.ForeignKey(
        "filesystem.File", on_delete=models.CASCADE, related_name="upload_files"
    )
    status = models.CharField(
        max_length=50, choices=UploadStatus.choices, default=UploadStatus.Initiated
    )
    started_at = models.DateTimeField(null=True)
    completed_at = models.DateTimeField(null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "upload_files"


class UploadChunk(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    upload_file = models.ForeignKey(
        "uploads.UploadFile", on_delete=models.CASCADE, related_name="chunks"
    )
    chunk = models.ForeignKey(
        "storage.Chunk", on_delete=models.CASCADE, related_name="upload_chunks"
    )
    status = models.CharField(
        max_length=50, choices=UploadStatus.choices, default=UploadStatus.Initiated
    )
    started_at = models.DateTimeField(null=True)
    completed_at = models.DateTimeField(null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "upload_chunks"
