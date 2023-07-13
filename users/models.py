from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Account(models.Model):
    owner=models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    platform=models.CharField(max_length=255)
    username=models.CharField(max_length=255)
    password=models.CharField(max_length=255)

    def __str__(self):
        return self.platform