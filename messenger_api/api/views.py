from dialogues.models import Dialogue, Message
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from djoser.views import UserViewSet
from rest_framework import mixins, viewsets

from .permissions import DialogPermission, MessagePermission
from .serializers import (DialogueCreateSerializer, DialogueSerializer,
                          MessageSerializer)


class CustomUserViewSet(UserViewSet):
    """Вьюсет для модели пользователей."""

    filter_backends = (DjangoFilterBackend,)
    filterset_fields = (
        "username",
        "email",
        "phone",
        "first_name",
        "last_name"
    )


class DialogueViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    """Вьюсет для модели диалогов."""

    permission_classes = (DialogPermission,)

    def get_serializer_class(self):
        if self.action == "create":
            return DialogueCreateSerializer
        return DialogueSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Dialogue.objects.filter(
            Q(first_user=user) | Q(second_user=user))
        return queryset


class MessageViewSet(
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    """Вьюсет для модели сообщений."""

    serializer_class = MessageSerializer
    permission_classes = (MessagePermission,)

    def get_queryset(self):
        user = self.request.user
        queryset = Message.objects.filter(sender=user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)
