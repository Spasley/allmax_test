from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


choices = ((1, "Very"), (2, "Slightly"), (3, "The future"))


class Record(models.Model):
    """Particular record in todo list"""
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_added = models.DateTimeField('date added', default=timezone.now())
    text = models.CharField(max_length=140)
    priority = models.IntegerField(choices=choices, default=1)
    is_active = models.BinaryField()


class CustomUser(AbstractUser):
    """Model required for serving user login using email instead of username"""

    def __str__(self):
        return self.email
