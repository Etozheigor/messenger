from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    """Модель пользователя."""

    avatar = models.ImageField(
        verbose_name="аватар", blank=True, null=True, upload_to="users_avatar"
    )
    phone = PhoneNumberField(
        verbose_name="телефон",
        unique=True,
        blank=True,
        null=True,
        help_text="Пример: +78001234567",
    )

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
