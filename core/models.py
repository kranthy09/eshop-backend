"""Database models for Core App"""

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """User model for Entire Application"""

    is_admin = models.BooleanField(default=False)
