from django.urls import path
from .views import RegistrationPageView, LoginPageView, ProfilePageView, \
    VerifyAccountView, DeleteFilmSerialRatingView, \
    DeleteFilmSerialFavoriteView, DeleteFilmSerialLaterView, \
    DeleteFilmSerialReviewView, ChangeUsernameView, EditReviewFilmView, \
    EditReviewSerialView

urlpatterns = [

    # register url
    path('register/', RegistrationPageView.as_view(), name='register_page'),

    # login url
    path('login/', LoginPageView.as_view(), name='login_page'),

    # profile url
    path('profile/<slug:username>', ProfilePageView.as_view(),
         name='profile_page'),

    # verify link
    path('verify/<slug:username>', VerifyAccountView.as_view(),
         name='verify_acc'),

    # edit film url
    path('edit_review_film/<slug:film_slug>/<slug:username>',
         EditReviewFilmView.as_view(),
         name='edit_review_film'),

    # edit serial url
    path('edit_review_serial/<slug:serial_slug>/<slug:username>',
         EditReviewSerialView.as_view(),
         name='edit_review_serial'),

    # ajax url

    # ajax delete film serial
    path('delete_film_serial/', DeleteFilmSerialRatingView.as_view(),
         name='delete_film_serial'),

    # ajax delete favorite film serial
    path('delete_film_serial_favorite/',
         DeleteFilmSerialFavoriteView.as_view(),
         name='delete_film_serial_favorite'),

    # ajax delete later film serial
    path('delete_film_serial_later/', DeleteFilmSerialLaterView.as_view(),
         name="delete_film_serial_later"),

    # ajax delete review film serial
    path('delete_film_serial_review/', DeleteFilmSerialReviewView.as_view(),
         name='delete_film_serial_review'),

    # ajax change username
    path('change_username_user/', ChangeUsernameView.as_view(),
         name='change_username_user'),
]
