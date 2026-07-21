from django import models


class UploadStatus(models.TextChoices):
    Initiated = "initiated", "Initiated"
    Uploading = "uploading", "Uploading"
    Verifying = "verifying", "Verifying"
    Replicating = "replicating", "Replicating"
    Completed = "completed", "Completed"
    Failed = "failed", "Failed"
    Canceled = "canceled", "Canceled"
    Expired = "expired", "Expired"
