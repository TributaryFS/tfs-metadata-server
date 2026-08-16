from apps.permissions.choices import Permission
from apps.permissions.models import DirectoryPermission

PERMISSION_RANK = {
    Permission.ORPHAN: 0,
    Permission.READ: 1,
    Permission.WRITE: 2,
    Permission.OWNER: 3,
}


def has_directory_permission(*, user, directory, required_permission):

    current_directory = directory

    while current_directory is not None:
        permission = (
            DirectoryPermission.objects.filter(user=user, directory=current_directory)
            .values_list("permission_level", flat=True)
            .first()
        )
        if permission:
            return PERMISSION_RANK[permission] >= PERMISSION_RANK[required_permission]

        current_directory = current_directory.parent_directory

    return False
