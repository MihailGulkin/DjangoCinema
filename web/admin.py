from django.contrib import admin
from .models import Genre, Director, Movie, Serial, Season, Episode, \
    ActionsWithSerial, ActionsWithMovie, UserRatingMovie

admin.site.register(Genre)
admin.site.register(Director)

admin.site.register(Movie)
admin.site.register(ActionsWithMovie)
admin.site.register(UserRatingMovie)

admin.site.register(ActionsWithSerial)
admin.site.register(Serial)
admin.site.register(Season)
admin.site.register(Episode)
