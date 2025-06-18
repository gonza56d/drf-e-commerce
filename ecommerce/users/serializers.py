from django.db import transaction
from ecommerce.profiles.models import Profile
from ecommerce.users.models import User

from rest_framework import serializers


class UserSignUpSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()

    def save(self, **kwargs) -> User:
        with transaction.atomic():
            user = User.objects.create_user(
                email=self.validated_data.get('email'),
                password=self.validated_data.get('password'),
            )
            Profile.objects.create(
                user=user,
                first_name=self.validated_data.get('first_name'),
                last_name=self.validated_data.get('last_name'),
                birthday=self.validated_data.get('birthday'),
            )
        return user
