import logging

from django.shortcuts import render
from django.views import View
from .models import Movie, Genre, Director
from web.service.shuffle_model import shuffle_model
from django.core.paginator import Paginator
from django.http import JsonResponse


class MainPageView(View):
    template = 'web/main.html'

    movie_model = Movie
    genres_model = Genre.objects.all()

    directors = [director.name for director in Director.objects.all()]
    film_genres = [{movie.title: [genre.name for genre in movie.genre.all()]}
                   for movie in movie_model.objects.all()]

    paginator = Paginator(movie_model.objects.all(), 9)
    first_page = paginator.page(1).object_list
    page_range = paginator.page_range

    def get(self, request):
        popular_movie_model_objects = \
            shuffle_model(self.movie_model, 10)
        return render(request, self.template,
                      {"popular_movies": popular_movie_model_objects,
                       'genres': self.genres_model,
                       'first_page': self.first_page,
                       'page_range': range(1, 4),
                       'total_pages': len(self.page_range)})

    def post(self, request):
        page_n = request.POST.get('page_n', None)
        results = list(
            self.paginator.page(page_n).object_list.values())
        return JsonResponse({"results": results,
                             'directors': self.directors,
                             'film_genres': self.film_genres})


class MoviePageView(View):
    template = 'web/movie_page.html'

    def get(self, request, slug):
        return render(request, self.template)
