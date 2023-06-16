from rest_framework import serializers

from core.models import User


class UserSerializer(serializers.ModelSerializer):
    """
    User model serializer.

    :param serializers.ModelSerializer: The base serializer.
    :type serializers.ModelSerializer: serializers.ModelSerializer
    """

    class Meta:
        """
        Meta class for the User model serializer.
        """

        #: model: The model to serialize.
        model = User

        #: fields: The fields to serialize.
        fields = [
            "id",
            "username",
            "password",
            "document",
            "is_admin",
            "is_staff",
            "created_at",
        ]
        extra_kwargs = {
            "is_admin": {"read_only": True},
            "is_staff": {"read_only": True},
            "created_at": {"read_only": True},
            "password": {"write_only": True},
            "document": {"read_only": True},
        }

    def create(self, validated_data):
        validated_data["is_admin"] = True
        validated_data["is_staff"] = True

        password = validated_data.pop("password")

        instance = self.Meta.model(**validated_data)
        instance.is_superuser = True
        instance.set_password(password)
        instance.save()

        return instance
