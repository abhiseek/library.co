
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    address = models.CharField(max_length=25)
    phone = models.IntegerField()

    is_superuser = models.BooleanField(default=False) #admin
    is_user = models.BooleanField(default=False) #normal user
    def __str__(self):
        return self.username

