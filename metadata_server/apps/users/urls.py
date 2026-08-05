from django.urls import path

from .views import ChangePasswordView, UserAPIView, UserDetailView

urlpatterns = [
    path("user/", UserAPIView.as_view()),
    path("user/<uuid:user_id>/", UserDetailView.as_view()),
    path("user/update_password/<uuid:user_id>/", ChangePasswordView.as_view()),
]
