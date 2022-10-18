from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """
    Custom user model with main e-mail field and verified flag
    for email verification
    """
    email = models.EmailField(max_length=64,
                              help_text='Enter a valid email address',
                              unique=True,
                              default='',
                              )
    is_verified = models.BooleanField('verified', default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']