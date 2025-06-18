from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):

    def create_user(self, email: str, password: str, is_admin: bool = False):
        user = User(email=email, is_staff=is_admin, is_superuser=is_admin)
        user.set_password(password)
        user.save()


class User(AbstractUser):

    username = None
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()
