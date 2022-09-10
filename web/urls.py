from django.urls import path, include
from .views import MainPageView, MoviePageView
urlpatterns = [
    path('', MainPageView.as_view(), name='main_page'),
    path('movie/<slug:slug>', MoviePageView.as_view(), name='movie_page'),

]
