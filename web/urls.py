from django.urls import path, include
from .views import MainPageView, MoviePageView, SerialPageView
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', MainPageView.as_view(), name='main_page'),
    path('movie/<slug:slug>/', MoviePageView.as_view(), name='movie_page'),
    path('serial/<slug:slug>/', SerialPageView.as_view(), name='serial_page'),


    path('favicon.ico', RedirectView.as_view(
        url=staticfiles_storage.url('image/favicon.ico')))

]
