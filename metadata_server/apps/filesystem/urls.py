from django.urls import path

from .views import DirectoryAPIView, DirectoryListCreateView, FileListCreateView

urlpatterns = [
    path("directories/old/", DirectoryListCreateView.as_view()),
    path("files/", FileListCreateView.as_view()),
    path("directories/", DirectoryAPIView.as_view()),
]
