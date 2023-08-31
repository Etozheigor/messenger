from rest_framework import permissions


class DialogPermission(permissions.BasePermission):
    """Пермишен для доступка к диалогам.

    Удаление доступно только участникам диалога.
    """

    message = "Доступно толко участникам диалогa"

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return request.user == obj.first_user or request == obj.second_user


class MessagePermission(permissions.BasePermission):
    """Пермишен для доступка к сообщениями.

    Удаление доступно только автору сообщения.
    """

    message = "Доступно только автору сообщения"

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return request.user == obj.sender
