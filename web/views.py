from django.views import View
from django.http import JsonResponse
from django.shortcuts import render
from django.core.paginator import Paginator

from .models import (Movie, Genre, Director, Serial, ActionsWithMovie,
                     ActionsWithSerial, UserRatingMovie, UserRatingSerial,
                     UserReviewMovie, UserReviewSerial,
                     UsersReviewLikeDislikeMovie, UsersReviewLikeDislikeSerial)

from .service.shuffle_model import shuffle_model
from .service.return_model_query import return_query
from .service.create_serial_film_model import \
    create_serial_film_model_response
from .service.mixins.response_film_serial_page import GetResponseMixin
from .service.mixins.calculate_review_percentage import \
    CalculateReviewsTypeMixin
from .service.mixins.return_new_review_response import GetNewUserReviewMixin
from .service.mixins.like_dislike_response import GetUsersLikeDis
from .service.mixins.favorite_later_movie import CheckFavLaterMovieMixin

TOTAL_PAGES = 9


class MainPageView(View, CheckFavLaterMovieMixin):
    template = 'web/main.html'

    movie_model = Movie
    serials = Serial.objects.all()

    directors = [director.name for director in Director.objects.all()]
    directors_href = [director.slug_field for director in
                      Director.objects.all()]
    film_genres = [{movie.title: [genre.name for genre in Genre.objects.all()]}
                   for movie in movie_model.objects.all()]

    paginator = Paginator(movie_model.objects.all(), TOTAL_PAGES)
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
                       'serials': self.serials})

    def post(self, request):
        page_n = request.POST.get('page_n', None)
        results = list(
            self.paginator.page(page_n).object_list.values())

        return JsonResponse({"results": results,
                             'directors': self.directors,
                             'directors_href': self.directors_href,
                             'film_genres': self.film_genres,
                             'favorite': self._favorite_later_movie(
                                 request,
                                 page_n,
                                 'Favorite',
                                 self.paginator
                             ),
                             'later': self._favorite_later_movie(
                                 request,
                                 page_n,
                                 'Later',
                                 self.paginator
                             )}
                            )


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


class GenrePageView(View, CheckFavLaterMovieMixin):
    template = 'web/genre.html'
    genre_model = Genre
    movie_model = Movie

    directors = [director.name for director in Director.objects.all()]
    directors_href = [director.slug_field for director in Director.objects.all()]

    film_genres = [{movie.title: [genre.name for genre in movie.genre.all()]}
                   for movie in movie_model.objects.all()]

    def get(self, request, genre_name):
        genre_object = self.genre_model.objects.get(slug=genre_name)
        movie_flt = self.movie_model.objects.filter(genre=genre_object)

        paginator = Paginator(movie_flt, TOTAL_PAGES)

        first_page = paginator.page(1).object_list
        page_range = paginator.page_range

        total_pages = len(page_range)

        return render(request, self.template,
                      {'genre_name': genre_object.name,
                       'first_page': first_page,
                       'page_range': range(1, 4) if total_pages >= 3 else
                       range(1, total_pages + 1),
                       'total_pages': total_pages
                       })

    def post(self, request, genre_name):
        genre_object = self.genre_model.objects.get(slug=genre_name)
        movie_flt = self.movie_model.objects.filter(genre=genre_object)

        paginator = Paginator(movie_flt, TOTAL_PAGES)

        page_n = request.POST.get('page_n', None)

        results = list(
            paginator.page(page_n).object_list.values())

        return JsonResponse({"results": results,
                             'directors': self.directors,
                             'directors_href': self.directors_href,
                             'film_genres': self.film_genres,
                             'favorite': self._favorite_later_movie(
                                 request,
                                 page_n,
                                 'Favorite',
                                 paginator
                             ),
                             'later': self._favorite_later_movie(
                                 request,
                                 page_n,
                                 'Later',
                                 paginator)})


class DirectorPageView(View):
    template = 'web/director.html'
    director_model = Director

    def get(self, request, director_name):
        director_obj = self.director_model.objects.get(
            slug_field=director_name)
        return render(request, self.template,
                      {'director': director_obj}
                      )


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
