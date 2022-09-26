from django.urls import path, include
from .views import MainPageView, MoviePageView, SerialPageView, \
    SearchAjaxView, GenrePageView, FavoriteView, GenresNavView
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
    path('<slug:genre_name>/', GenrePageView.as_view(), name='genre_page'),


    path('search_search_url_search_token', SearchAjaxView.as_view(),
         name='search_form'),
    path('favorite_film', FavoriteView.as_view(), name='love_click'),
    path('genres_menu', GenresNavView.as_view(), name='genre_nav'),

    path('favicon.ico', RedirectView.as_view(
        url=staticfiles_storage.url('image/favicon.ico')))

]
