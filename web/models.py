from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

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
    genre = models.ManyToManyField('Genre')
    poster = models.ImageField(upload_to='Movie/Posters/')
    movie_page_poster = models.ImageField(upload_to='Movie/Posters/MoviePage/',
                                          null=True, blank=True)
    summary = models.TextField(max_length=1600)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']
