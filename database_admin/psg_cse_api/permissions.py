from django.contrib.auth.decorators import user_passes_test
from rest_framework import permissions


class IsCalcUser(permissions.BasePermission):
    @user_passes_test
    def has_object_permission(self, request, view, obj):
        return bool(request.user.groups.filter(name='CalcUser').exists())


