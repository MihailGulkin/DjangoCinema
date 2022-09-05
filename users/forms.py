from .models import CustomUser
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm


class CustomUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'password1', 'password2']

