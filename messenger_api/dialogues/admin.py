from django.contrib import admin

from .models import Dialogue, Message

admin.site.register(Message)
admin.site.register(Dialogue)
