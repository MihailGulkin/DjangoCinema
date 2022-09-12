from django.urls import path, include
from .views import MainPageView, MoviePageView, SerialPageView
urlpatterns = [
    path('', MainPageView.as_view(), name='main_page'),
    path('movie/<slug:slug>/', MoviePageView.as_view(), name='movie_page'),
    path('serial/<slug:slug>/', SerialPageView.as_view(), name='serial_page'),

]
