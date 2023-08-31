from django.db import models
from users.models import User


class Dialogue(models.Model):
    """Модель диалогов."""

    first_user = models.ForeignKey(
        User,
        verbose_name="Пользователь 1",
        on_delete=models.SET_NULL,
        null=True,
        related_name="created_dialogues",
    )
    second_user = models.ForeignKey(
        User,
        verbose_name="Пользователь 2",
        on_delete=models.SET_NULL,
        null=True,
        related_name="dialogues",
    )

    class Meta:
        verbose_name = "Диалог"
        verbose_name_plural = "Диалоги"


class Message(models.Model):
    """Модель сообщений."""

    dialogue = models.ForeignKey(
        Dialogue,
        verbose_name="диалог",
        on_delete=models.CASCADE,
        related_name="messages",
    )
    sender = models.ForeignKey(
        User,
        verbose_name="отправитель",
        on_delete=models.SET_NULL,
        null=True,
        related_name="sent_messages",
    )
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"
