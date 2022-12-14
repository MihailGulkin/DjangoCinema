from re import fullmatch

from django.views import View
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login
from django.contrib.auth.forms import AuthenticationForm

from .models import CustomUser
from .forms import CustomUserForm

from web.models import UserRatingMovie, UserRatingSerial, ActionsWithMovie, \
    ActionsWithSerial, UserReviewSerial, UserReviewMovie, Movie, Serial

from users.tasks import send_first_verify_email, send_already_verified_email

from .service.delete_requiered_field import delete_field
from .service.verify import verify_user
from .service.mixins.delete_profile_data import DeleteProfileDataMixin
from .service.mixins.edit_review_base import EditReviewBaseMixin


class RegistrationPageView(View):
    """
    Registration CBV with GET and POST method, with send e-mail function
    and validation form.
    """
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
            logout(request)
            send_first_verify_email.delay(
                request.build_absolute_uri('/'),
                request.POST['username'],
                request.POST['email']
            )
            return redirect('login_page')
        return redirect('register_page')


class LoginPageView(View):
    """
    Login CBV with GET and POST method with validation form.
    """
    template = 'users/login.html'
    user_form = AuthenticationForm

    def get(self, request):
        return render(request, self.template,
                      {'user_form': self.user_form()})

    def post(self, request):
        if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            form = self.user_form(request, data=request.POST)

            if not form.is_valid():
                return JsonResponse({'errors': form.errors})

            user = form.get_user()

            if not verify_user(user.username):
                return JsonResponse({'errors': {
                    'verify': False,
                    'verify_url': f'{request.build_absolute_uri("/")}verify/{user.username}'}})

            login(request, user)

            return JsonResponse(
                {
                    'url': f'{request.build_absolute_uri(f"/profile/{request.user.username}")}'
                })


class VerifyAccountView(View):
    """
    CBV with GET method, to handle verify url.
    """
    user_model = CustomUser
    template = 'users/login.html'
    user_form = AuthenticationForm

    def get(self, request, username):
        user = self.user_model.objects.get(
            username=username
        )
        if user.is_verified:
            return redirect('main_page')

        send_already_verified_email.delay(
            username,
            user.email
        )

        user.is_verified = True
        user.save()

        return render(request, self.template,
                      {'user_form': self.user_form(),
                       'verify_flag': True})


class ProfilePageView(View):
    """
    Profile CBV for only GET method to return models data.
    """
    template = 'users/profile.html'

    def get(self, request, username):
        user_obj = CustomUser.objects.filter(username=username)
        if not user_obj.exists():
            return redirect('main_page')
        user_obj = user_obj.first()
        user_films = UserRatingMovie.objects.filter(user=user_obj)
        user_serial = UserRatingSerial.objects.filter(user=user_obj)

        user_favorite_later_film = ActionsWithMovie.objects.filter(
            user=user_obj
        )
        user_favorite_later_serial = ActionsWithSerial.objects.filter(
            user=user_obj
        )
        user_favorite_film, user_later_film = user_favorite_later_film.filter(
            choose_favorite_later='Favorite'
        ), user_favorite_later_film.filter(
            choose_favorite_later='Later'
        )
        user_favorite_serial, user_later_serial = user_favorite_later_serial.filter(
            choose_favorite_later='Favorite'
        ), user_favorite_later_serial.filter(
            choose_favorite_later='Later'
        )
        user_review_film, user_review_serial = UserReviewMovie.objects.filter(
            user=user_obj
        ), UserReviewSerial.objects.filter(user=user_obj)
        return render(request, self.template, {
            'user_obj': user_obj,

            'user_films': user_films,
            'user_serials': user_serial,

            'user_favorite_films': user_favorite_film,
            'user_favorite_serials': user_favorite_serial,
            'user_later_films': user_later_film,
            'user_later_serials': user_later_serial,

            'user_review_films': user_review_film,
            'user_review_serials': user_review_serial,

            'flag_auth': True if request.user.username == username else False,

        })


# Ajax web View only

class DeleteFilmSerialRatingView(View, DeleteProfileDataMixin):
    """
    Full AJAX CBV to delete film and serial rating in profile.
    """

    def post(self, request):
        if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            rating_serials = UserRatingSerial.objects.filter(user=request.user)
            rating_films = UserRatingMovie.objects.filter(user=request.user)
            slug = request.POST['slug']

            if request.POST['type'] == 'film':
                return self._delete_profile_data_film_serial(
                    rating_films.get(
                        movie=self._return_movie_obj(slug)
                    ),
                    rating_films
                )
            return self._delete_profile_data_film_serial(rating_serials.get(
                serial=self._return_serial_obj(slug)
            ),
                rating_serials
            )


class DeleteFilmSerialFavoriteView(View, DeleteProfileDataMixin):
    """
    Full AJAX CBV to delete film and serial from favorite.
    """

    def post(self, request):
        if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            favorite_films = ActionsWithMovie.objects.filter(
                user=request.user,
                choose_favorite_later='Favorite'
            )
            favorite_serials = ActionsWithSerial.objects.filter(
                user=request.user,
                choose_favorite_later='Favorite'
            )
            slug = request.POST['slug']

            if request.POST['type'] == 'film':
                return self._delete_profile_data_film_serial(
                    favorite_films.get(
                        cinema_type=self._return_movie_obj(slug)
                    ),
                    favorite_films
                )
            return self._delete_profile_data_film_serial(favorite_serials.get(
                cinema_type=self._return_serial_obj(slug)
            ),
                favorite_serials
            )


class DeleteFilmSerialLaterView(View, DeleteProfileDataMixin):
    """
    Full AJAX CBV to delete film and serial from later.
    """

    def post(self, request):
        if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            later_films = ActionsWithMovie.objects.filter(
                user=request.user,
                choose_favorite_later='Later'
            )
            later_serials = ActionsWithSerial.objects.filter(
                user=request.user,
                choose_favorite_later='Later'
            )
            slug = request.POST['slug']

            if request.POST['type'] == 'film':
                return self._delete_profile_data_film_serial(
                    later_films.get(
                        cinema_type=self._return_movie_obj(slug)
                    ),
                    later_films
                )
            return self._delete_profile_data_film_serial(later_serials.get(
                cinema_type=self._return_serial_obj(slug)
            ),
                later_serials
            )


class DeleteFilmSerialReviewView(View, DeleteProfileDataMixin):
    """
    Full AJAX CBV to delete film and serial user review in profile.
    """

    def post(self, request):
        if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            review_films = UserReviewMovie.objects.filter(
                user=request.user,
            )
            review_serials = UserReviewSerial.objects.filter(
                user=request.user,
            )
            slug = request.POST['slug']

            if request.POST['type'] == 'film':
                return self._delete_profile_data_film_serial(
                    review_films.get(
                        movie=self._return_movie_obj(slug)
                    ),
                    review_films
                )
            return self._delete_profile_data_film_serial(
                review_serials.get(
                    serial=self._return_serial_obj(slug)
                ),
                review_serials
            )


class ChangeUsernameView(View):
    """
    Full AJAX CBV to change username in settings tab in profile.
    """

    def post(self, request):
        if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            username = request.POST['username']
            if CustomUser.objects.filter(
                    username=username).exists() and \
                    request.user.username != username:
                return JsonResponse(
                    {'data': {'error': 'Username already exist'}})
            if not fullmatch(r'[A-Za-z\d]*', username):
                return JsonResponse(
                    {'data': {'error': 'Only letters and numeric'}}
                )
            if request.user.username == username:
                return JsonResponse({'data': {}})
            user_obj = CustomUser.objects.get(username=request.user.username)
            user_obj.username = username
            user_obj.save()
            return JsonResponse({'data': {
                'url': f'/profile/{username}'}
            })


class EditReviewFilmView(View, EditReviewBaseMixin):
    """
    CBV to edit user film review with POST-AJAX and GET method.
    """

    def get(self, request, film_slug, username):
        film_obj = Movie.objects.filter(slug=film_slug).first()
        review_obj = UserReviewMovie.objects.filter(movie=film_obj)

        return self._return_get_response(request, username, review_obj)

    def post(self, request, film_slug, username):
        film_obj = Movie.objects.filter(slug=film_slug).first()
        review_obj = UserReviewMovie.objects.filter(
            movie=film_obj,
        )
        return self._return_post_response(request, username, review_obj)


class EditReviewSerialView(View, EditReviewBaseMixin):
    """
    CBV to edit user serial review with POST-AJAX and GET method.
    """

    def get(self, request, serial_slug, username):
        serial_obj = Serial.objects.filter(slug=serial_slug).first()
        review_obj = UserReviewSerial.objects.filter(
            serial=serial_obj,
        )
        return self._return_get_response(request, username, review_obj)

    def post(self, request, serial_slug, username):
        serial_obj = Serial.objects.filter(slug=serial_slug).first()
        review_obj = UserReviewSerial.objects.filter(
            serial=serial_obj,
        )
        return self._return_post_response(request, username, review_obj)
