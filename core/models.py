from django.contrib.auth.models import AbstractUser
from core.managers import CustomUserManager
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = None
    objects = CustomUserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []



