from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

from .views import ChangePasswordView, LoginView, UserDetailView, UserListCreateView

urlpatterns = [
    path("register_user/", UserListCreateView.as_view()),
    path("user/<uuid:user_id>/", UserDetailView.as_view()),
    path("user/update_password/", ChangePasswordView.as_view()),
    path("auth/login/", LoginView.as_view()),
    path("auth/refresh/", TokenRefreshView.as_view()),
]
