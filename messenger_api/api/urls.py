from django.urls import include, path
from djoser.views import UserViewSet
from rest_framework.routers import DefaultRouter

from .views import CustomUserViewSet, DialogueViewSet, MessageViewSet

app_name = "api"

v1_router = DefaultRouter()

v1_router.register("dialogues", DialogueViewSet, basename="dialogue")
v1_router.register("messages", MessageViewSet, basename="message")

urlpatterns = [
    path("", include(v1_router.urls)),
    path(
        "users/",
        CustomUserViewSet.as_view({"post": "create", "get": "list"}),
        name="user",
    ),
    path(
        "users/me/",
        UserViewSet.as_view({"get": "me", "patch": "me"}),
        name="user-me",
    ),
    path("auth/", include("djoser.urls.jwt")),
]
