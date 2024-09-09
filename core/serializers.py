from rest_framework import serializers

from core.models import Bibliotecario, User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    group_name = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            "provider",
            "email",
            "password",
            "profile_picture",
            "is_active",
            "groups",
            "group_name",
        ]
        depth = 1


class BibliotecarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bibliotecario
        fields = "__all__"
