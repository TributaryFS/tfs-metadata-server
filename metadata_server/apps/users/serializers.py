from apps.filesystem.models import Directory
from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        self.create_root_dir(validated_data.get("id"))
        return User.objects.create(**validated_data)

    @staticmethod
    def create_root_dir(user_id):
        data = {"name": "/", "owner": user_id, "parent_directory": None}
        Directory(data=data)
