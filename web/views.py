import logging

from django.shortcuts import render
from django.views import View
from .models import Movie, Genre
from web.service.shuffle_model import shuffle_model
from django.core.paginator import Paginator
from django.http import JsonResponse

class MainPageView(View):
    template = 'web/main.html'
    movie_model = Movie
    genres_model = Genre.objects.all()

    paginatorr = Paginator(movie_model.objects.all(), 9)
    first_page = paginatorr.page(1).object_list
    page_range = paginatorr.page_range

    def get(self, request):
        popular_movie_model_objects = \
            shuffle_model(self.movie_model, 10)
        return render(request, self.template,
                      {"popular_movies": popular_movie_model_objects,
                       'genres': self.genres_model,
                       'paginator': self.paginatorr,
                       'first_page': self.first_page,
                       'page_range': self.page_range})

    def post(self, request):
        page_n = request.POST.get('page_n', None)  # getting page number
        results = list(
            self.paginatorr.page(page_n).object_list.values())

        return JsonResponse({"results": results})
