from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    email=models.EmailField(unique=True,blank=False)

    def __str__(self):
        return str(self.username)