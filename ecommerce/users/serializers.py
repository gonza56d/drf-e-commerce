from ecommerce.users.models import User

from rest_framework import serializers


class UserSignUpSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()

    def create(self, validated_data):
        User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
        )
