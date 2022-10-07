from django.urls import path, include
from .views import MainPageView, MoviePageView, SerialPageView, \
    SearchAjaxView, GenrePageView, FavoriteView, GenresNavView, LaterView, \
    DeleteRatingUserView, SendReviewUserView, UserLikeDislikeReviewView
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', MainPageView.as_view(), name='main_page'),
    path('logout/', LogoutView.as_view(), name='logout_page'),
    path('movie/<slug:movie_name>/', MoviePageView.as_view(),
         name='movie_page'),
    path('serial/<slug:serial_name>/', SerialPageView.as_view(),
         name='serial_page'),
    path('genre/<slug:genre_name>/', GenrePageView.as_view(),
         name='genre_page'),

    # ajaxed path for only post view
    path('user_review_like_dislike', UserLikeDislikeReviewView.as_view(),
         name="like_dislike_review"),
    path('review_user_send', SendReviewUserView.as_view(), name="review_user"),
    path('delete_user_rating', DeleteRatingUserView.as_view(),
         name='delete_user_rating'),
    path('later_film', LaterView.as_view(), name='later_click'),
    path('search_search_url_search_token', SearchAjaxView.as_view(),
         name='search_form'),
    path('favorite_film', FavoriteView.as_view(), name='love_click'),
    path('genres_menu', GenresNavView.as_view(), name='genre_nav'),

    path('favicon.ico', RedirectView.as_view(
        url=staticfiles_storage.url('image/favicon.ico')))

]
