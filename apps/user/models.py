from django.contrib.auth.models import AbstractUser
from django.db import models
from .manager import UserManager

class User(AbstractUser):

    STATUS = (
        ('regular', 'regular'),
        ('moderator', 'moderator')
    )

    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    email = models.EmailField(max_length=254, unique=True)
    status = models.CharField(max_length=50, choices=STATUS, default='regular')
    bio = models.TextField(max_length=600, blank=True, default='')
    photo = models.CharField(max_length=250, default='', null=True)
    name = models.CharField(max_length=250)

    objects = UserManager()

    def __str__(self) -> str:
        return self.email
