from apps.permissions.choices import Permission
from apps.permissions.services import has_directory_permission
from rest_framework.permissions import BasePermission


class DirectoryPermissionRequired(BasePermission):
    required_permission = Permission.ORPHAN

    def has_object_permission(self, request, view, obj):

        return has_directory_permission(
            user=request.user,
            directory=obj,
            required_permission=self.required_permission,
        )


class CanReadDirectory(DirectoryPermissionRequired):
    required_permission = Permission.READ


class CanWriteDirectory(DirectoryPermissionRequired):
    required_permission = Permission.WRITE


class CanOwnDirectory(DirectoryPermissionRequired):
    required_permission = Permission.OWNER
