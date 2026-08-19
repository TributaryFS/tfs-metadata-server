from apps.filesystem.models import Directory
from apps.permissions.choices import Permission
from apps.permissions.models import DirectoryPermission
from apps.permissions.services import has_directory_permission
from django.db import IntegrityError, transaction
from rest_framework.exceptions import PermissionDenied, ValidationError


def _ensure_name_is_available(*, parent_directory, name, excluding_directory=None):
    directories = Directory.objects.filter(parent_directory=parent_directory, name=name)
    if excluding_directory is not None:
        directories = directories.exclude(pk=excluding_directory.pk)

    if directories.exists():
        raise ValidationError(
            {"name": ["A directory with this name already exists here."]}
        )


@transaction.atomic
def create_directory(*, user, name, parent_directory):
    if not has_directory_permission(
        user=user, directory=parent_directory, required_permission=Permission.WRITE
    ):
        raise PermissionDenied("You do not have permission to create a directory here.")

    _ensure_name_is_available(parent_directory=parent_directory, name=name)
    try:
        with transaction.atomic():
            directory = Directory.objects.create(
                owner=user,
                parent_directory=parent_directory,
                name=name,
            )
    except IntegrityError as error:
        raise ValidationError(
            {"name": ["A directory with this name already exists here."]}
        ) from error
    DirectoryPermission.objects.create(
        directory=directory, user=user, permission_level=Permission.OWNER
    )

    return directory


@transaction.atomic
def rename_directory(*, user, directory, new_name):
    if not has_directory_permission(
        user=user, directory=directory, required_permission=Permission.OWNER
    ):
        raise PermissionDenied("You do not have permission to rename the directory")

    _ensure_name_is_available(
        parent_directory=directory.parent_directory,
        name=new_name,
        excluding_directory=directory,
    )
    try:
        with transaction.atomic():
            directory.name = new_name
            directory.save(update_fields=["name", "updated_at"])
    except IntegrityError as error:
        raise ValidationError(
            {"name": ["A directory with this name already exists here."]}
        ) from error

    return directory
