from django.shortcuts import render
from django.views import View
from .forms import UserCreationForm


class RegistrationPageView(View):
    template = 'users/test.html'
    user_form = UserCreationForm

    def get(self, request):
        return render(request, self.template,
                      {'user_form': self.user_form(),
                       'value': 'dsfsdf1'})
