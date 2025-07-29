from django.contrib.auth.models import User
from django.db import models


class userProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/', null=True, blank=True)


def __str__(self):
    return self.user.username
