from django.contrib.auth.models import User, AbstractUser
from django.db import models

from DjangoProject4 import settings


class userProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/', null=True, blank=True)


def __str__(self):
    return self.user.username

# class CustomUser(AbstractUser):
#     ROLE_CHOICES = [
#         ('user', 'User'),
#         ('admin', 'Admin'),
#         ('superadmin', 'Super Admin'),
#     ]
#     role = models.CharField(max_length=15, choices=ROLE_CHOICES, default='user')
#
#     def __str__(self):
#         return f"{self.username} ({self.role})"