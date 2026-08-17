from django.urls import path

from .views import DirectoryAPIView, DirectoryDetailView

urlpatterns = [
    path("create_directory/", DirectoryAPIView.as_view()),
    path("directory/<uuid:directory_id>/", DirectoryDetailView.as_view()),
]
