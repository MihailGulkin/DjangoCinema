from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from django import forms


class CustomUserForm(UserCreationForm):
    """
    User creation form with overloading clean method to check valid username
    and clean_password2 method to check only ascii letters password
    """
    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'password1', 'password2']

    def clean(self):
        username = self.cleaned_data.get('username')
        if self._check_ascii(username if username else ''):
            raise forms.ValidationError(
                'Sorry, only ascii characters'
            )
        return self.cleaned_data

    def clean_password2(self):
        super(CustomUserForm, self).clean_password2()
        pwd2 = self.cleaned_data.get('password2')
        if self._check_ascii(pwd2):
            self.add_error('password2', 'Only ascii characters')
        return pwd2

    def _check_ascii(self, some_error_string: str) -> bool:
        for char in some_error_string:
            if not char.isascii():
                return True
        return False
