from django.shortcuts import render
from django.views import View
from .models import Movie

class MainPageView(View):
    template = 'web/main.html'
    movie_model = Movie.objects.all()
    def get(self, request):
        return render(request, self.template, {"movies": self.movie_model})
