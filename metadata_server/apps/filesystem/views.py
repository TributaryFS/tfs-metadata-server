from apps.filesystem.permissions import CanReadDirectory
from apps.filesystem.services import create_directory
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Directory
from .serializers import DirectorySerializer


class DirectoryListCreateView(APIView):
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
    permission_classes = [IsAuthenticated, CanReadDirectory]  # noqa: RUF012

    def get(self, request, directory_id):
        directory = get_object_or_404(Directory, id=directory_id)
        # There is another security design where you filter the queryset according to permissions so unauthorized objects also appear as 404.

        self.check_object_permissions(request, directory)

        serializer = DirectorySerializer(directory)

        return Response(serializer.data)
