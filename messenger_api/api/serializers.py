from dialogues.models import Dialogue, Message
from djoser.serializers import UserSerializer
from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers
from users.models import User

from messenger_api.settings import MESSAGES_LIMIT


class CustomUserSerializer(UserSerializer):
    """Сериализатор для модели User."""

    avatar = Base64ImageField(required=False)

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "avatar",
            "phone"
        )


class MessageDialogueSerializer(serializers.ModelSerializer):
    """Сериализатор для отображения сообщений в диалоге."""

    class Meta:
        model = Message
        fields = ("id", "sender", "text", "date")


class MessageSerializer(serializers.ModelSerializer):
    """Сериализатор длясообщений."""

    class Meta:
        model = Message
        fields = ("dialogue", "text")

    def validate_dialogue(self, value):
        user = self.context["request"].user
        if value.first_user != user and value.second_user != user:
            raise serializers.ValidationError(
                "Невозможно отправить сообщение в этот диалог."
            )
        return value


class DialogueSerializer(serializers.ModelSerializer):
    """Сериализатор для диалогов."""

    messages = serializers.SerializerMethodField()

    class Meta:
        model = Dialogue
        fields = ("id", "first_user", "second_user", "messages")

    def get_messages(self, obj):
        if self.context["request"].query_params.get("messages_limit"):
            limit = int(
                self.context["request"].query_params.get("messages_limit"))
        else:
            limit = MESSAGES_LIMIT
        messages = MessageDialogueSerializer(
            obj.messages.all(), many=True).data
        messages_list = [msg for msg in messages]
        messages_list.sort(key=lambda d: d["date"], reverse=True)
        return messages_list[:limit]


class DialogueCreateSerializer(serializers.ModelSerializer):
    """Сериализатор для создания диалогов."""

    username = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Dialogue
        fields = ("username",)

    def validate_username(self, value):
        if not User.objects.filter(username=value).exists():
            raise serializers.ValidationError(
                "Пользователя с таким username не существует!"
            )
        second_user = User.objects.get(username=value)
        if (
            Dialogue.objects.filter(
                first_user=self.context[
                    "request"].user, second_user=second_user
            ).exists()
            or Dialogue.objects.filter(
                first_user=second_user, second_user=self.context[
                    "request"].user
            ).exists()
        ):
            raise serializers.ValidationError(
                "Диалог с этим пользователем уже существует!"
            )
        if self.context["request"].user == second_user:
            raise serializers.ValidationError(
                "Невозможно начать диалог с самим собой!")
        return value

    def create(self, validated_data):
        second_user = User.objects.get(username=validated_data["username"])
        dialogue = Dialogue.objects.create(
            first_user=self.context["request"].user, second_user=second_user
        )
        dialogue.save()
        return dialogue
