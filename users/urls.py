from django.urls import path
from .views import RegistrationPageView, LoginPageView, ProfilePageView, \
    VerifyAccountView, DeleteFilmSerialRatingView, \
    DeleteFilmSerialFavoriteView, DeleteFilmSerialLaterView, \
    DeleteFilmSerialReviewView, ChangeUsernameView, EditReviewFilmView, \
    EditReviewSerialView

urlpatterns = [
    path('register/', RegistrationPageView.as_view(), name='register_page'),
    path('login/', LoginPageView.as_view(), name='login_page'),
    path('profile/<slug:username>', ProfilePageView.as_view(),
         name='profile_page'),
    path('verify/<slug:username>', VerifyAccountView.as_view(),
         name='verify_acc'),
    path('edit_review_film/<slug:film_slug>/<slug:username>',
         EditReviewFilmView.as_view(),
         name='edit_review_film'),
    path('edit_review_serial/<slug:serial_slug>/<slug:username>',
         EditReviewSerialView.as_view(),
         name='edit_review_serial'),

    path('delete_film_serial/', DeleteFilmSerialRatingView.as_view(),
         name='delete_film_serial'),
    path('delete_film_serial_favorite/',
         DeleteFilmSerialFavoriteView.as_view(),
         name='delete_film_serial_favorite'),
    path('delete_film_serial_later/', DeleteFilmSerialLaterView.as_view(),
         name="delete_film_serial_later"),
    path('delete_film_serial_review/', DeleteFilmSerialReviewView.as_view(),
         name='delete_film_serial_review'),
    path('change_username_user/', ChangeUsernameView.as_view(),
         name='change_username_user'),
]
