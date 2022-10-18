from django.urls import path
from .views import MainPageView, MoviePageView, SerialPageView, \
    SearchAjaxView, GenrePageView, FavoriteView, GenresNavView, LaterView, \
    DeleteRatingUserView, SendReviewUserView, UserLikeDislikeReviewView, \
    DirectorPageView
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from django.contrib.auth.views import LogoutView

urlpatterns = [

    # Home page
    path('', MainPageView.as_view(), name='main_page'),

    # LogOutUrl
    path('logout/', LogoutView.as_view(), name='logout_page'),

    # Movie Page
    path('movie/<slug:movie_name>/', MoviePageView.as_view(),
         name='movie_page'),

    # Serial Page
    path('serial/<slug:serial_name>/', SerialPageView.as_view(),
         name='serial_page'),

    # Genre Page
    path('genre/<slug:genre_name>/', GenrePageView.as_view(),
         name='genre_page'),

    # Director Page
    path('director/<slug:director_name>/', DirectorPageView.as_view(),
         name='director_page'),

    # Ajax url

    # Ajax for add like/dislike user under movie and serial review
    path('user_review_like_dislike', UserLikeDislikeReviewView.as_view(),
         name="like_dislike_review"),

    # Ajax for send user movie/serial review
    path('review_user_send', SendReviewUserView.as_view(), name="review_user"),

    # Ajax delete user rating under movie/serial page
    path('delete_user_rating', DeleteRatingUserView.as_view(),
         name='delete_user_rating'),

    # Ajax for append film in later category
    path('later_film', LaterView.as_view(), name='later_click'),

    # Ajax for append film in favorite category
    path('favorite_film', FavoriteView.as_view(), name='love_click'),

    # Ajax for dynamically search
    path('search_search_url_search_token', SearchAjaxView.as_view(),
         name='search_form'),

    # Ajax for genres menu
    path('genres_menu', GenresNavView.as_view(), name='genre_nav'),

    # Ico url
    path('favicon.ico', RedirectView.as_view(
        url=staticfiles_storage.url('image/favicon.ico')))

]
