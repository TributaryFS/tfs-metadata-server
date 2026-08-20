from django.urls import path

from .views import DirectoryAPIView, DirectoryChildrenView, DirectoryDetailView

urlpatterns = [
    path("create_directory/", DirectoryAPIView.as_view()),
    path("directory/<uuid:directory_id>/", DirectoryDetailView.as_view()),
    path("directories/<uuid:directory_id>/children/", DirectoryChildrenView.as_view()),
]
