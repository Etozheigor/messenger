# Generated by Django 4.2.4 on 2023-08-31 17:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("dialogues", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="message",
            name="sender",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="sent_messages",
                to=settings.AUTH_USER_MODEL,
                verbose_name="отправитель",
            ),
        ),
        migrations.AddField(
            model_name="dialogue",
            name="first_user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="created_dialogues",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Пользователь 1",
            ),
        ),
        migrations.AddField(
            model_name="dialogue",
            name="second_user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="dialogues",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Пользователь 2",
            ),
        ),
    ]
