from apps.filesystem.models import Directory
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError as DjangoValidationError
from django.db import transaction
from rest_framework import serializers

from .models import User


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "password", "email"]  # noqa: RUF012
        read_only_fields = ["id"]  # noqa: RUF012

    def create(self, validated_data):
        with transaction.atomic():
            user = User.objects.create_user(**validated_data)
            self._create_root_directory(user)
            return user

    @staticmethod
    def _create_root_directory(user):
        Directory.objects.create(
            name="/",
            owner=user,
        )


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "email"]  # noqa: RUF012


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]  # noqa: RUF012


class PasswordUpdateSerializer(serializers.Serializer):
    old_password = serializers.CharField(
        write_only=True, required=True, trim_whitespace=False
    )
    new_password = serializers.CharField(
        write_only=True, required=True, trim_whitespace=False
    )

    def validate_old_password(self, value):
        user = self.context["request"].user

        if not user.check_password(value):
            raise serializers.ValidationError("Incorrect Password.")

        return value

    def validate(self, attrs):
        # 1. Confirm passwords match
        if attrs["new_password"] != attrs["confirm_password"]:
            raise serializers.ValidationError(
                {"confirm_password": "New password and confirmation do not match."}
            )

        # 2. Prevent setting the same password
        if attrs["old_password"] == attrs["new_password"]:
            raise serializers.ValidationError(
                {"new_password": "New password cannot be the same as the old password."}
            )

        # 3. Apply Django's built-in password policies (AUTH_PASSWORD_VALIDATORS)
        user = self.context["request"].user
        try:
            validate_password(password=attrs["new_password"], user=user)
        except DjangoValidationError as e:
            raise serializers.ValidationError({"new_password": list(e.messages)})

        return attrs

    def save(self, **kwargs):
        user = self.context["request"].user

        user.set_password(self.validated_data["new_password"])
        user.save(update_fields=["password"])
