from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    contact = models.CharField(max_length=150, blank=True)