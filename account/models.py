from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    name = models.CharField(max_length=255)
    contact = models.CharField(max_length=20)
    role=models.CharField(max_length=20,blank=True,null=True)

    def __str__(self):
        return self.username
