from apps.permissions.choices import Permission
from apps.permissions.models import DirectoryPermission

PERMISSION_RANK = {
    Permission.ORPHAN: 0,
    Permission.READ: 1,
    Permission.WRITE: 2,
    Permission.OWNER: 3,
}


def has_directory_permission(user, directory, required_permission):
    permission = (
        DirectoryPermission.objects.filter(user=user, directory=directory)
        .values_list("permission_level", flat=True)
        .first()
    )
    if not permission:
        return False

    return PERMISSION_RANK[permission] >= PERMISSION_RANK[required_permission]
