from web.models import FavoriteMovie
from django import template

register = template.Library()


@register.filter(name='favorite')
def favorite(movie: int):
    return FavoriteMovie.objects.filter(movie=movie).exists()
