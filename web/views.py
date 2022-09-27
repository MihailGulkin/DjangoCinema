from django.shortcuts import render
from django.views import View
from .models import Movie, Genre, Director, Serial, ActionsWithMovie, \
    ActionsWithSerial
from web.service.shuffle_model import shuffle_model
from django.core.paginator import Paginator
from django.http import JsonResponse
from web.service.return_model_query import return_query


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
                             'favorite': self._favorite_movie(request,
                                                              page_n)})

    def _favorite_movie(self, request, page_n):
        if request.user.is_authenticated:
            return [ActionsWithMovie.objects.filter(cinema_type=film,
                                                 user=request.user,
                                                 choose_favorite_later='Favorite').exists()
                    for film in self.paginator.page(page_n).object_list]
        return [False for _ in range(len(page_n))]


class MoviePageView(View):
    template = 'web/movie_page.html'
    movie = Movie

    def get(self, request, movie_name):
        return render(request, self.template,
                      {'content': self.movie.objects.get(slug=movie_name),
                       })


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
            self.slug = request.POST.get('slug')
            if request.POST.get('cinema_type') == 'film':
                return self._create_serial_film_model(Movie, ActionsWithMovie,
                                                      request)
            return self._create_serial_film_model(Serial, ActionsWithSerial,
                                                  request)

    def _create_serial_film_model(self, model_cinema, favorite_cinema,
                                  request):
        _obj = model_cinema.objects.get(slug=self.slug)
        if favorite_cinema.objects.filter(user=request.user,
                                          cinema_type=_obj,
                                          choose_favorite_later='Favorite').exists():
            favorite_cinema.objects.get(user=request.user,
                                        cinema_type=_obj,
                                        choose_favorite_later='Favorite').delete()
            return JsonResponse({'dataRemove': {'slug': self.slug}})
        favorite_cinema.objects.create(user=request.user,
                                       cinema_type=_obj,
                                       choose_favorite_later='Favorite')

        return JsonResponse({'dataAdd': {'slug': self.slug}})
