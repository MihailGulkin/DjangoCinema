import logging

from django.shortcuts import render, redirect
from django.views import View
from .forms import CustomUserForm
from django.http import JsonResponse
from .service.delete_requiered_field import delete_field
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout, login
from .service.send_email_ import send_first_verify_email, \
    send_already_verified_email
from .service.verify import verify_user
from .models import CustomUser


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
            send_first_verify_email(
                request,
                request.POST['username'],
                request.POST['email']
            )
            return redirect('login_page')
        return redirect('register_page')


class LoginPageView(View):
    template = 'users/login.html'
    user_form = AuthenticationForm

    def get(self, request):
        return render(request, self.template,
                      {'user_form': self.user_form()})

    def post(self, request):
        if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            form = self.user_form(request, data=request.POST)

            if not form.is_valid():
                return JsonResponse({'errors': form.errors})

            user = form.get_user()

            if not verify_user(user.username):
                return JsonResponse({'errors': {
                    'verify': False,
                    'verify_url': f'{request.build_absolute_uri("/")}verify/{user.username}'}})

            login(request, user)

            return JsonResponse(
                {
                    'url': f'{request.build_absolute_uri(f"/profile/{request.user.username}")}'
                })


class VerifyAccountView(View):
    user_model = CustomUser
    template = 'users/login.html'
    user_form = AuthenticationForm

    def get(self, request, username):
        user = self.user_model.objects.get(
                username=username
            )
        if user.is_verified:
            return redirect('main_page')

        send_already_verified_email(
            username,
            user.email
        )

        user.is_verified = True
        user.save()

        return render(request, self.template,
                      {'user_form': self.user_form(),
                       'verify_flag': True})


class ProfilePageView(View):
    template = 'users/profile.html'

    def get(self, request, username):
        return render(request, self.template)
