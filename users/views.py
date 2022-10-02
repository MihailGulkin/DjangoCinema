import logging

from django.shortcuts import render, redirect
from django.views import View
from .forms import CustomUserForm
from django.http import JsonResponse
from .service.delete_requiered_field import delete_field
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout, login


class RegistrationPageView(View):
    template = 'users/register.html'
    user_form = CustomUserForm

    def get(self, request):
        return render(request, self.template,
                      {'user_form': self.user_form()})

    def post(self, request):
        form = self.user_form(request.POST)
        if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            if form.is_valid():
                return JsonResponse({'errors': ''})
            return JsonResponse({'errors': delete_field(dict(form.errors))})
        if form.is_valid():
            form.save()
            logout(request)
            return redirect('login_page')
        return redirect('register_page')


class LoginPageView(View):
    template = 'users/login.html'

    def get(self, request):
        return render(request, self.template,
                      {'user_form': AuthenticationForm()})

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return JsonResponse(
                {
                    'url': f'{request.build_absolute_uri(f"/profile/{request.user.username}")}'
                })
        return JsonResponse({'errors': form.errors})


class ProfilePageView(View):
    template = 'users/profile.html'

    def get(self, request, username):
        return render(request, self.template)
