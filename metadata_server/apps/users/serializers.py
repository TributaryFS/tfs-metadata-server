from apps.filesystem.models import Directory
from django.db import transaction
from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        with transaction.atomic():
            user = super().create(validated_data)
            self._create_root_directory(user)
            return user

    @staticmethod
    def _create_root_directory(user):
        Directory.objects.create(
            name="/",
            owner=user,
        )
