from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Directory, File
from .serializers import DirectorySerializer, FileSerializer


class DirectoryListCreateView(generics.ListCreateAPIView):
    queryset = Directory.objects.all()
    serializer_class = DirectorySerializer


class FileListCreateView(generics.ListCreateAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer


class DirectoryAPIView(APIView):
    def get(self, request):
        dir_qs = Directory.objects.all()
        serializer = DirectorySerializer(dir_qs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DirectorySerializer(data=request.data)

        if serializer.is_valid():
            directory = serializer.save()
            return Response(
                DirectorySerializer(directory).data, status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
