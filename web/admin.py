from django.contrib import admin

from .models import Genre, Director, Movie, Serial, Season, Episode, \
    ActionsWithSerial, ActionsWithMovie, UserRatingMovie, UserRatingSerial, \
    UserReviewMovie


class ActionMovieAdmin(admin.ModelAdmin):
    list_display = ('user', 'cinema_type', 'choose_favorite_later', 'created')


class UserRatingMovieAdmin(admin.ModelAdmin):
    list_display = ('user', 'movie', 'rating', 'created')


class UserRatingSerialAdmin(admin.ModelAdmin):
    list_display = ('user', 'serial', 'rating', 'created')


admin.site.register(Genre)
admin.site.register(Director)

admin.site.register(Movie)
admin.site.register(ActionsWithMovie, ActionMovieAdmin)
admin.site.register(UserRatingMovie, UserRatingMovieAdmin)
admin.site.register(UserReviewMovie)

admin.site.register(ActionsWithSerial, ActionMovieAdmin)
admin.site.register(UserRatingSerial, UserRatingSerialAdmin)
admin.site.register(Serial)
admin.site.register(Season)
admin.site.register(Episode)
