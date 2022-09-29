from django.contrib import admin
from .models import Genre, Director, Movie, Serial, Season, Episode, \
    ActionsWithSerial, ActionsWithMovie, UserRatingMovie


class ActionMovieAdmin(admin.ModelAdmin):
    list_display = ('user', 'cinema_type', 'choose_favorite_later', 'created')


admin.site.register(Genre)
admin.site.register(Director)

admin.site.register(Movie)
admin.site.register(ActionsWithMovie, ActionMovieAdmin)
admin.site.register(UserRatingMovie)

admin.site.register(ActionsWithSerial, ActionMovieAdmin)
admin.site.register(Serial)
admin.site.register(Season)
admin.site.register(Episode)
