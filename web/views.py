from django.shortcuts import render
from django.views import View


class MainPageView(View):
    template = 'web/main.html'

    def get(self, request):
        return render(request, self.template)
