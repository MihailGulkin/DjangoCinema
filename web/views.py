from django.shortcuts import render
from django.views import View
from .models import Movie, Genre
import logging


class MainPageView(View):
    template = 'web/main.html'
    movie_model = Movie.objects.all()
    genres_model = Genre.objects.all()

    def get(self, request):
        return render(request, self.template, {"movies": self.movie_model,
                                               'genres': self.genres_model})
