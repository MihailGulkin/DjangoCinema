from django.db import models
from django.utils.text import slugify


class Genre(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, null=True)

    def __str__(self):
        return self.name


class Director(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=200)
    director = models.ForeignKey('Director', on_delete=models.CASCADE,
                                 default=None)
    release_date = models.CharField(max_length=70, default='None')
    short_intro = models.TextField(max_length=700)

    IMDb_RATING = models.CharField(max_length=50, default=None)
    genre = models.ManyToManyField('Genre', default=None)
    poster = models.ImageField(upload_to='Movie/Posters/')
    movie_page_poster = models.ImageField(upload_to='Movie/Posters/MoviePage/',
                                          null=True, blank=True)
    summary = models.TextField(max_length=1600)

    created = models.DateTimeField(auto_now_add=True)

    slug = models.SlugField(unique=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']


class Serial(models.Model):
    Serial_name = models.CharField(max_length=200)

    director = models.ForeignKey('Director', on_delete=models.CASCADE,
                                 default=None)

    release_date = models.CharField(max_length=70, default='None')

    end_date = models.CharField(max_length=70, default='None')

    short_intro = models.TextField(max_length=700)

    IMDb_RATING = models.CharField(max_length=50, default=None)

    genre = models.ManyToManyField('Genre')

    poster = models.ImageField(upload_to='Movie/Posters/')

    seriel_page_poster = models.ImageField(
        upload_to='Movie/Posters/SerialPage/',
        null=True, blank=True)

    summary = models.TextField(max_length=1600)

    seasons = models.ManyToManyField('Season', default=None)

    created = models.DateTimeField(auto_now_add=True)

    slug = models.SlugField(unique=True, null=True, default='slug')

    def __str__(self):
        return self.Serial_name

    class Meta:
        ordering = ['-created']


# Season - Serial
class Season(models.Model):
    season_name = models.CharField(max_length=50, default='S01 - Serial Name')
    Episodes = models.ManyToManyField('Episode', default=None)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.season_name

    class Meta:
        ordering = ['-season_name']


# Episode - Serial
class Episode(models.Model):
    chose_season = models.ForeignKey('Season', on_delete=models.CASCADE,
                                     default=None, null=True, blank=True)

    episode_number = models.CharField(max_length=50,
                                      default='E01 - Serial Name')

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.episode_number
