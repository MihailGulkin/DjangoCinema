from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, null=True, )

    def __str__(self):
        return self.name


class Director(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    poster = models.ImageField(upload_to='Directors/')
    born_place = models.CharField(max_length=100)
    born_date = models.CharField(max_length=100)

    def __str__(self):
        return self.name


mpa_rating_system = [('G', 'G'),
                     ('PG', 'PG'),
                     ('PG-13', 'PG-13'),
                     ('R', 'R'),
                     ('NC-17', 'NC-17')
                     ]

age_rating_system = [('0', '0'),
                     ('6+', '6+'),
                     ('12+', '12+'),
                     ('16+', '16+'),
                     ('18+', '18+')]


class Movie(models.Model):
    title = models.CharField(max_length=200)

    director = models.ForeignKey('Director', on_delete=models.CASCADE,
                                 default=None)

    release_date = models.CharField(max_length=70, default='None')

    short_intro = models.TextField(max_length=700)

    IMDb_RATING = models.CharField(max_length=50, default=None)

    genre = models.ManyToManyField('Genre', default=None)

    poster = models.ImageField(upload_to='Movie/Posters/')

    summary = models.TextField(max_length=1600)

    country = models.CharField(max_length=100, default='Russia')

    created = models.DateTimeField(auto_now_add=True)

    slug = models.SlugField(unique=True, null=True)

    time_minute = models.PositiveIntegerField(default=1)

    age_rating_sys = models.CharField(max_length=100,
                                      choices=age_rating_system)
    mpa_rating_sys = models.CharField(max_length=100,
                                      choices=mpa_rating_system)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']

    def get_model_name(self):
        return self._meta.model_name


class FavoriteMovie(models.Model):
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE,
                             default=None)
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE,
                              default=None)

    def __str__(self):
        return f'{self.user.username} - {self.movie}'


class FavoriteSerial(models.Model):
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE,
                             default=None)
    serial = models.ForeignKey('Serial', on_delete=models.CASCADE,
                               default=None)

    def __str__(self):
        return f'{self.user.username} - {self.serial}'


class Serial(models.Model):
    serial_name = models.CharField(max_length=200)

    director = models.ForeignKey('Director', on_delete=models.CASCADE,
                                 default=None)

    release_date = models.CharField(max_length=70, default='None')

    end_date = models.CharField(max_length=70, default='None')

    short_intro = models.TextField(max_length=700)

    IMDb_RATING = models.CharField(max_length=50, default=None)

    genre = models.ManyToManyField('Genre')

    poster = models.ImageField(upload_to='Movie/Posters/')

    summary = models.TextField(max_length=1600)

    seasons = models.ManyToManyField('Season', default=None)

    created = models.DateTimeField(auto_now_add=True)

    country = models.CharField(max_length=100, default='Russia')

    time_minute = models.PositiveIntegerField(default=1)

    slug = models.SlugField(unique=True, null=True, default='slug')

    age_rating_sys = models.CharField(max_length=100,
                                      choices=age_rating_system)
    mpa_rating_sys = models.CharField(max_length=100,
                                      choices=mpa_rating_system)

    def __str__(self):
        return self.serial_name

    class Meta:
        ordering = ['-created']

    def get_model_name(self):
        return self._meta.model_name


# Season - Serial
class Season(models.Model):
    season_name = models.CharField(max_length=50, default='S01 - Serial Name')
    Episodes = models.ManyToManyField('Episode', default=None)
    number_episodes = models.PositiveIntegerField(default=1)
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
