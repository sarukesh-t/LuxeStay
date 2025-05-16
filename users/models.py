from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    class Meta:
        swappable = "AUTH_USER_MODEL"
