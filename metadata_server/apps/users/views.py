from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializers import (
    PasswordUpdateSerializer,
    UserCreateSerializer,
    UserDetailSerializer,
    UserUpdateSerializer,
)


class UserAPIView(APIView):
    def get(self, request):
        user_qs = User.objects.all()
        serializer = UserDetailSerializer(user_qs, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response(UserDetailSerializer(user).data, status.HTTP_201_CREATED)


class UserDetailView(APIView):
    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        serializer = UserDetailSerializer(user)

        return Response(serializer.data)

    def patch(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        serializer = UserUpdateSerializer(user, data=request.data, partial=True)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(UserDetailSerializer(user).data, status.HTTP_200_OK)


class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]  # noqa: RUF012

    def post(self, request):
        serializer = PasswordUpdateSerializer(
            data=request.data, context={"request": request}
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"detail": "Password updated successfully"}, status.HTTP_200_OK)
