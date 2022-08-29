from rest_framework import serializers
from .models import UserPSG


class UserPSGSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = UserPSG
        fields = "__all__"







