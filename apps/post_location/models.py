from email.policy import default
from django.db import models
from apps.user.models import User
from datetime import datetime

class PostLocation(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    location = models.JSONField(default={})
    photo = models.CharField(max_length=254)
    comments = models.TextField(default='', max_length=600, null=True, blank=True)
    created_at = models.DateTimeField(null=True, default=datetime.now())

