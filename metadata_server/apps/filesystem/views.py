from apps.filesystem.permissions import CanOwnDirectory, CanReadDirectory
from apps.filesystem.services import create_directory, rename_directory
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Directory
from .serializers import DirectoryRenameSerializer, DirectorySerializer


class DirectoryAPIView(APIView):
    permission_classes = [IsAuthenticated]  # noqa: RUF012

    def post(self, request):
        serializer = DirectorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        parent_directory = serializer.validated_data.get("parent_directory")  # type: ignore

        if parent_directory is None:
            parent_directory = request.user.root_directory

        directory = create_directory(
            user=request.user,
            parent_directory=parent_directory,
            name=serializer.validated_data["name"],  # type: ignore
        )
        return Response(
            DirectorySerializer(directory).data, status=status.HTTP_201_CREATED
        )


class DirectoryDetailView(APIView):
    def get_permissions(self):
        if self.request.method == "GET":
            return [
                IsAuthenticated(),
                CanReadDirectory(),
            ]

        if self.request.method == "PATCH":
            return [
                IsAuthenticated(),
                CanOwnDirectory(),
            ]

        return [
            IsAuthenticated(),
        ]

    def get(self, request, directory_id):
        directory = get_object_or_404(Directory, id=directory_id)
        # There is another security design where you filter the queryset according to permissions so unauthorized objects also appear as 404.

        self.check_object_permissions(request, directory)

        serializer = DirectorySerializer(directory)

        return Response(serializer.data)

    def patch(self, request, directory_id):
        directory = get_object_or_404(Directory, id=directory_id)
        self.check_object_permissions(request, directory)

        serializer = DirectoryRenameSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        directory = rename_directory(
            user=self.request.user,
            directory=directory,
            new_name=serializer.validated_data["name"],
        )
        return Response(
            DirectorySerializer(directory).data,
            status=status.HTTP_200_OK,
        )
