from rest_framework import serializers

from .models import Directory, File


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = "__all__"


class DirectorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Directory
        fields = "__all__"

    def create(self, validated_data):
        parent_dir = validated_data.get("parent_directory")
        if not parent_dir:
            parent_dir = self.get_user_root(validated_data.get("owner"))

        validated_data["parent_directory"] = parent_dir

        return Directory.objects.create(**validated_data)

    @staticmethod
    def get_user_root(owner):
        return Directory.objects.get(owner=owner, paren_directory=None)
