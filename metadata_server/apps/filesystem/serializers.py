from rest_framework import serializers

from .models import Directory, File


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = [  # noqa: RUF012
            "id",
            "name",
            "local_path",
            "parent_directory",
            "size",
            "last_modified",
            "last_modified_by",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [  # noqa: RUF012
            "id",
            "created_at",
            "updated_at",
        ]


class DirectorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Directory
        fields = [  # noqa: RUF012
            "id",
            "name",
            "parent_directory",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [  # noqa: RUF012
            "id",
            "created_at",
            "updated_at",
        ]


class DirectoryRenameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Directory
        fields = ["name"]  # noqa: RUF012
