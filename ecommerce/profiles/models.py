from django.db import models


class Profile(models.Model):

    user = models.ForeignKey('users.User', on_delete=models.CASCADE, null=False, related_name='profiles')
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    birth_date = models.DateField()
