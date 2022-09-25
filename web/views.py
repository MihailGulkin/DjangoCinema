import logging

from django.shortcuts import render
from django.views import View
from .models import Movie, Genre, Director, Serial, FavoriteMovie
from users.models import CustomUser
from web.service.shuffle_model import shuffle_model
from django.core.paginator import Paginator
from django.http import JsonResponse
from web.service.return_model_query import return_query
from django.contrib.auth.mixins import LoginRequiredMixin


class MainPageView(View):
    template = 'web/main.html'

    movie_model = Movie
    genres_model = Genre.objects.all()
    serial = Serial.objects.get(pk=1)

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
                       'total_pages': len(self.page_range),
                       'serial': self.serial})

    def post(self, request):
        page_n = request.POST.get('page_n', None)
        results = list(
            self.paginator.page(page_n).object_list.values())

        return JsonResponse({"results": results,
                             'directors': self.directors,
                             'film_genres': self.film_genres,
                             'favorite': self._favorite_movie(request,
                                                               page_n)})

    def _favorite_movie(self, request, page_n):
        return [FavoriteMovie.objects.filter(movie=film,
                                             user=request.user).exists()
                for film in self.paginator.page(page_n).object_list]


class MoviePageView(View):
    template = 'web/movie_page.html'
    movie = Movie
    genres_model = Genre.objects.all()

    def get(self, request, movie_name):
        return render(request, self.template,
                      {'content': self.movie.objects.get(slug=movie_name),
                       'genres': self.genres_model})


class SerialPageView(View):
    template = 'web/serial_page.html'
    serial = Serial
    genres_model = Genre.objects.all()

    def get(self, request, serial_name):
        return render(request, self.template,
                      {'content': self.serial.objects.get(slug=serial_name),
                       'genres': self.genres_model})


class GenrePageView(View):
    template = 'web/genre.html'
    genres_model = Genre.objects.all()

    def get(self, request, genre_name):
        return render(request, self.template,
                      {'genres': self.genres_model})


class SearchAjaxView(View):
    def post(self, request):
        if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':

            query = request.POST.get('query')

            query_film = Movie.objects.filter(title__contains=query)
            query_se = Serial.objects.filter(serial_name__contains=query)

            if (len(query_film) or len(query_se)) and len(query):
                return JsonResponse(
                    {'data': return_query(list(query_se.values()),
                                          list(query_film.values()),
                                          number_element=3)})
            return JsonResponse({'data': 'No result :('})
        return JsonResponse({})


class FavoriteView(View):

    def post(self, request):
        if not request.user.is_authenticated:
            return JsonResponse(
                {'url': f'{request.build_absolute_uri("register/")}'})

        if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            slug_movie = request.POST.get('slug')
            movie_obj = Movie.objects.get(slug=slug_movie)
            if FavoriteMovie.objects.filter(user=request.user,
                                            movie=movie_obj).exists():
                FavoriteMovie.objects.get(user=request.user,
                                          movie=movie_obj).delete()
                return JsonResponse({'dataRemove': {'slug': slug_movie}})
            FavoriteMovie.objects.create(user=request.user,
                                         movie=Movie.objects.get(
                                             slug=slug_movie))

            return JsonResponse(
                {'dataAdd': {'slug': slug_movie}})
