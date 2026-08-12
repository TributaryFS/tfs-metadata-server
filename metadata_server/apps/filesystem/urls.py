from django.urls import path

from .views import DirectoryDetailView, DirectoryListCreateView

urlpatterns = [
    path("directories/", DirectoryListCreateView.as_view()),
    path("directories/<uuid:directory_id>/", DirectoryDetailView.as_view()),
]
