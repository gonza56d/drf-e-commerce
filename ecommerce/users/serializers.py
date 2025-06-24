from django.db import transaction
from ecommerce.profiles.models import Profile
from ecommerce.profiles.serializers import ProfileSerializer
from ecommerce.users.models import User

from rest_framework import serializers


class UserSignUpSerializer(serializers.ModelSerializer):

    first_name = serializers.CharField(max_length=256, write_only=True)
    last_name = serializers.CharField(max_length=256, write_only=True)
    birth_date = serializers.DateField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'birth_date']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def save(self, **kwargs) -> User:
        with transaction.atomic():
            user = User.objects.create_user(
                email=self.validated_data.get('email'),
                username=self.validated_data.get('username'),
                password=self.validated_data.get('password'),
            )
            Profile.objects.create(
                user=user,
                first_name=self.validated_data.get('first_name'),
                last_name=self.validated_data.get('last_name'),
                birth_date =self.validated_data.get('birth_date'),
            )
        return user


class UserSerializer(serializers.ModelSerializer):
    profiles = ProfileSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ['username', 'profiles']
