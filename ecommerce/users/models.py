from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):

    def create_user(self, email: str, username: str, password: str, is_admin: bool = False) -> 'User':
        user = self.model(email=email, username=username, is_staff=is_admin, is_superuser=is_admin)
        user.set_password(password)
        user.save()
        return user


class User(AbstractUser):

    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = UserManager()
