from django.contrib import admin
from .models import Genre, Director, Movie, Serial, Season, Episode, \
    FavoriteMovie, FavoriteSerial

admin.site.register(Genre)
admin.site.register(Director)

admin.site.register(Movie)
admin.site.register(FavoriteMovie)

admin.site.register(FavoriteSerial)
admin.site.register(Serial)
admin.site.register(Season)
admin.site.register(Episode)
