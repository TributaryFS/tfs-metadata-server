from apps.filesystem.models import Directory
from apps.permissions.choices import Permission
from apps.permissions.models import DirectoryPermission
from apps.permissions.services import has_directory_permission
from django.db import transaction
from rest_framework.exceptions import PermissionDenied


@transaction.atomic
def create_directory(user, name, parent_directory):
    if not has_directory_permission(
        user=user, directory=parent_directory, required_permission=Permission.WRITE
    ):
        raise PermissionDenied("You do not have permission to create a directory here.")

    directory = Directory.objects.create(
        owner=user,
        parent_directory=parent_directory,
        name=name,
    )
    DirectoryPermission.objects.create(
        directory=directory, user=user, permission_level=Permission.OWNER
    )

    return directory
