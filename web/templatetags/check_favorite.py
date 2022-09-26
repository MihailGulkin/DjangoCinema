from web.models import FavoriteMovie, FavoriteSerial
from django import template

register = template.Library()


@register.filter(name='favorite_movie')
def favorite_movie(movie, request):
    if request.user.is_authenticated:
        return FavoriteMovie.objects.filter(movie=movie,
                                            user=request.user).exists()
    return False


@register.filter(name='favorite_serial')
def favorite_serial(serial, request):
    if request.user.is_authenticated:
        return FavoriteSerial.objects.filter(serial=serial,
                                             user=request.user).exists()
    return False
