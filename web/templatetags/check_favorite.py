from web.models import ActionsWithMovie, ActionsWithSerial
from django import template

register = template.Library()


@register.filter(name='favorite_movie')
def favorite_movie(movie, request):
    if request.user.is_authenticated:
        return ActionsWithMovie.objects.filter(cinema_type=movie,
                                               user=request.user,
                                               choose_favorite_later='Favorite').exists()
    return False


@register.filter(name='favorite_serial')
def favorite_serial(serial, request):
    if request.user.is_authenticated:
        return ActionsWithSerial.objects.filter(cinema_type=serial,
                                                user=request.user,
                                                choose_favorite_later='Favorite').exists()
    return False
