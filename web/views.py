import logging

from django.shortcuts import render
from django.views import View
from .models import Movie, Genre, Director, Serial, ActionsWithMovie, \
    ActionsWithSerial, UserRatingMovie
from web.service.shuffle_model import shuffle_model
from django.core.paginator import Paginator
from django.http import JsonResponse
from web.service.return_model_query import return_query
from web.service.create_serial_film_model import \
    create_serial_film_model_response


class MainPageView(View):
    template = 'web/main.html'

    movie_model = Movie
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
                             'favorite': self._favorite_later_movie(request,
                                                                    page_n,
                                                                    'Favorite'),
                             'later': self._favorite_later_movie(request,
                                                                 page_n,
                                                                 'Later')})

    def _favorite_later_movie(self, request, page_n, choose):
        if request.user.is_authenticated:
            return [ActionsWithMovie.objects.filter(cinema_type=film,
                                                    user=request.user,
                                                    choose_favorite_later=choose).exists()
                    for film in self.paginator.page(page_n).object_list]
        return [False for _ in range(len(page_n))]


class MoviePageView(View):
    template = 'web/movie_page.html'
    movie = Movie
    movie_rating = UserRatingMovie

    def get(self, request, movie_name):
        movie_obj = self.movie.objects.get(slug=movie_name)
        if self.movie_rating.objects.filter(user=request.user,
                                            movie=movie_obj):
            pass
        return render(request, self.template,
                      {'content': self.movie.objects.get(slug=movie_name),
                       'rating': UserRatingMovie})

    def post(self, request, movie_name):
        logging.error(request.POST)
        logging.error(movie_name)
        return JsonResponse({'some': 'info'})


class SerialPageView(View):
    template = 'web/serial_page.html'
    serial = Serial

    def get(self, request, serial_name):
        return render(request, self.template,
                      {'content': self.serial.objects.get(slug=serial_name),
                       })


class GenrePageView(View):
    template = 'web/genre.html'

    def get(self, request, genre_name):
        return render(request, self.template)


# ajax web view only
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


class GenresNavView(View):
    genres_model = Genre.objects.all()

    def post(self, request):
        if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            return JsonResponse({'data': list(self.genres_model.values())})


class FavoriteView(View):

    def post(self, request):
        if not request.user.is_authenticated:
            return JsonResponse(
                {'url': f'{request.build_absolute_uri("register/")}'})

        if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            slug = request.POST.get('slug')
            if request.POST.get('cinema_type') == 'film':
                return create_serial_film_model_response(Movie,
                                                         ActionsWithMovie,
                                                         'Favorite',
                                                         request, slug)
            return create_serial_film_model_response(Serial, ActionsWithSerial,
                                                     'Favorite',
                                                     request, slug)


class LaterView(View):
    def post(self, request):
        if not request.user.is_authenticated:
            return JsonResponse(
                {'url': f'{request.build_absolute_uri("register/")}'})

        if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            slug = request.POST.get('slug')
            if request.POST.get('cinema_type') == 'film':
                return create_serial_film_model_response(Movie,
                                                         ActionsWithMovie,
                                                         'Later',
                                                         request, slug)
            return create_serial_film_model_response(Serial, ActionsWithSerial,
                                                     'Later',
                                                     request, slug)
