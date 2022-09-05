from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = models.EmailField(max_length=64,
                              help_text='Enter a valid email address',
                              unique=True,
                              default='',
                              )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']