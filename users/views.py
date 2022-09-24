import logging

from django.shortcuts import render, redirect
from django.views import View
from .forms import CustomUserForm
from django.http import JsonResponse
from .service.delete_requiered_field import delete_field


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
            return redirect('main_page')
        return redirect('register_page')
