from django.urls import path

from .views import DirectoryDetailView, DirectoryListCreateView

urlpatterns = [
    path("create_directory/", DirectoryListCreateView.as_view()),
    path("directory/<uuid:directory_id>/", DirectoryDetailView.as_view()),
]
