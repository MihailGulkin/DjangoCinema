from django.shortcuts import render
from django.views import View
from .models import (Movie, Genre, Director, Serial, ActionsWithMovie,
                     ActionsWithSerial, UserRatingMovie, UserRatingSerial,
                     UserReviewMovie, UserReviewSerial,
                     UsersReviewLikeDislikeMovie, UsersReviewLikeDislikeSerial)
from web.service.shuffle_model import shuffle_model
from django.core.paginator import Paginator
from django.http import JsonResponse
from web.service.return_model_query import return_query
from web.service.create_serial_film_model import \
    create_serial_film_model_response

from web.service.mixins.response_film_serial_page import GetResponseMixin
from web.service.mixins.calculate_review_percentage import \
    CalculateReviewsTypeMixin
from web.service.mixins.return_new_review_response import GetNewUserReviewMixin
from web.service.mixins.like_dislike_response import GetUsersLikeDis


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
                             'favorite': self._favorite_later_movie(
                                 request,
                                 page_n,
                                 'Favorite'
                             ),
                             'later': self._favorite_later_movie(
                                 request,
                                 page_n,
                                 'Later')})

    def _favorite_later_movie(self, request, page_n, choose):
        if request.user.is_authenticated:
            return [ActionsWithMovie.objects.filter(
                cinema_type=film,
                user=request.user,
                choose_favorite_later=choose).exists()
                    for film in self.paginator.page(page_n).object_list]
        return [False for _ in range(len(page_n))]


class MoviePageView(View, GetResponseMixin, CalculateReviewsTypeMixin):
    template = 'web/movie_page.html'
    model_obj = Movie
    model_review = UserReviewMovie
    rating = UserRatingMovie
    _type = 'film'

    def get(self, request, movie_name):
        model_obj = self.model_obj.objects.get(slug=movie_name)
        _review = self.model_review.objects.filter(movie=model_obj)
        filter_rating = self.rating.objects.filter(movie=model_obj)
        return self.get_response_film_serial(request, model_obj,
                                             _review, filter_rating)

    def post(self, request, movie_name):
        model_obj = self.model_obj.objects.get(slug=movie_name)
        filter_rating = self.rating.objects.filter(movie=model_obj)
        return self.post_response_film_serial(request, model_obj,
                                              filter_rating)

    def _create_rating_model(self, request, model_obj):
        rating_obj = self.rating.objects.create(
            user=request.user,
            movie=model_obj,
            rating=request.POST['rating'])
        return rating_obj


class SerialPageView(View, GetResponseMixin, CalculateReviewsTypeMixin):
    template = 'web/serial_page.html'
    model_obj = Serial
    rating = UserRatingSerial
    model_review = UserReviewSerial
    _type = 'serial'

    def get(self, request, serial_name):
        model_obj = self.model_obj.objects.get(slug=serial_name)
        _review = self.model_review.objects.filter(serial=model_obj)
        filter_rating = self.rating.objects.filter(serial=model_obj)
        return self.get_response_film_serial(request, model_obj,
                                             _review, filter_rating)

    def post(self, request, serial_name):
        model_obj = self.model_obj.objects.get(slug=serial_name)
        filter_rating = self.rating.objects.filter(serial=model_obj)
        return self.post_response_film_serial(request, model_obj,
                                              filter_rating)

    def _create_rating_model(self, request, model_obj):
        rating_obj = self.rating.objects.create(
            user=request.user,
            serial=model_obj,
            rating=request.POST['rating'])
        return rating_obj


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


class DeleteRatingUserView(View):
    def post(self, request):
        if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            if request.POST['type'] == 'film':
                movie_obj = Movie.objects.get(title=request.POST['name'])
                if x := UserRatingMovie.objects.filter(user=request.user,
                                                       movie=movie_obj).first():
                    x.delete()
                return JsonResponse({})
            serial_obj = Serial.objects.get(serial_name=request.POST['name'])
            if x := UserRatingSerial.objects.filter(user=request.user,
                                                    serial=serial_obj).first():
                x.delete()
            return JsonResponse({})


class SendReviewUserView(View, CalculateReviewsTypeMixin,
                         GetNewUserReviewMixin):
    model_review = UserReviewMovie

    def post(self, request):
        if not request.user.is_authenticated:
            return JsonResponse(
                {'url': f'{request.build_absolute_uri("register/")}'}
            )
        self.cinema_type, self.title, self.text_data, self.slug, self.review_type = (
            request.POST['type'],
            request.POST['title'],
            request.POST['text_data'],
            request.POST['slug'],
            request.POST['review_type'])
        if self.cinema_type == 'film':
            _obj = Movie.objects.get(slug=self.slug)
            return self.new_review_response(_obj, UserReviewMovie,
                                            UserReviewMovie.objects.filter(
                                                movie=_obj))
        _obj = Serial.objects.get(slug=self.slug)
        return self.new_review_response(_obj, UserReviewSerial,
                                        UserReviewSerial.objects.filter(
                                            serial=_obj))


class UserLikeDislikeReviewView(View, GetUsersLikeDis):
    def post(self, request):
        if not request.user.is_authenticated:
            return JsonResponse(
                {'url': f'{request.build_absolute_uri("register/")}'}
            )

        self.user, self.like_dislike, self.pk, self.cinema_type = (
            request.user, request.POST['value'],
            request.POST['pk'],
            request.POST['cinema_type']
        )
        if self.cinema_type == 'film':
            return self._return_like_dis_response(
                UserReviewMovie,
                UsersReviewLikeDislikeMovie
            )
        return self._return_like_dis_response(
            UserReviewSerial,
            UsersReviewLikeDislikeSerial
        )
