from django.db import models

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

favorite_later_cinema = [('Later', 'Later'),
                         ('Favorite', 'Favorite')]

type_of_review = [('Positive', 'Positive'),
                  ('Neutral', 'Neutral'),
                  ('Negative', 'Negative')]

like_dislike_review = [('Like', 'Like'),
                       ('Dislike', 'Dislike')]


class Genre(models.Model):
    """
    Genre model, contains all genres to use in Movie and Serial model's
    """
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, null=True, )

    def __str__(self):
        return self.name


class Director(models.Model):
    """
    Director model, contains all directors to use in Movie and Serial model's
    """
    name = models.CharField(max_length=200)

    created = models.DateTimeField(auto_now_add=True)
    poster = models.ImageField(upload_to='Directors/')
    born_place = models.CharField(max_length=100)
    born_date = models.DateTimeField()
    growth = models.CharField(max_length=100, default=None, null=True)
    genres = models.ManyToManyField('Genre', default=None)

    slug_field = models.SlugField(unique=True, null=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    """
    Movie model, contains movie director, genre, poster and etc.
    """
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


class Serial(models.Model):
    """
    Serial model, contains serial director, genre, poster, seasons and etc.
    """
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


class Season(models.Model):
    """
    Seasons model, contains many to many field on episode model
    """
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
    """
    Episode model, contains ForeignKey on season
    """
    chose_season = models.ForeignKey('Season', on_delete=models.CASCADE,
                                     default=None, null=True, blank=True)

    episode_number = models.CharField(max_length=50,
                                      default='E01 - Serial Name')

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.episode_number


class ActionsWithMovie(models.Model):
    """
    Model to note movie. User can choose: favorite or later.
    """
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE,
                             default=None)
    cinema_type = models.ForeignKey('Movie', on_delete=models.CASCADE,
                                    default=None)
    choose_favorite_later = models.CharField(max_length=100,
                                             choices=favorite_later_cinema,
                                             default='F')
    created = models.DateTimeField(auto_now_add=True,
                                   null=True)

    def __str__(self):
        return f'{self.user.username} - {self.cinema_type}'


class ActionsWithSerial(models.Model):
    """
    Model to note serial. User can choose: favorite or later.
    """
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE,
                             default=None)
    cinema_type = models.ForeignKey('Serial', on_delete=models.CASCADE,
                                    default=None)
    choose_favorite_later = models.CharField(max_length=100,
                                             choices=favorite_later_cinema,
                                             default='F')
    created = models.DateTimeField(auto_now_add=True,
                                   null=True)

    def __str__(self):
        return f'{self.user.username} - {self.cinema_type}'


class UserRatingMovie(models.Model):
    """
    Model to contains user movie rating
    """
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE,
                             default=None)
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE,
                              default=None)
    rating = models.PositiveSmallIntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True,
                                   null=True)

    def __str__(self):
        return f'{self.user.username} - {self.movie.title} - {self.rating}'


class UserRatingSerial(models.Model):
    """
    Model to contains user serial rating
    """
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE,
                             default=None)
    serial = models.ForeignKey('Serial', on_delete=models.CASCADE,
                               default=None)
    rating = models.PositiveSmallIntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True,
                                   null=True)

    def __str__(self):
        return f'{self.user.username} - {self.serial.serial_name} - ' \
               f'{self.rating}'


class UserReviewMovie(models.Model):
    """
    Contains user movies review. Have ForeignKey on Movie model
    """
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE,
                             default=None)
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE,
                              default=None)
    review_type = models.CharField(max_length=100,
                                   choices=type_of_review)
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=10_000)
    created = models.DateTimeField(auto_now_add=True,
                                   null=True)

    def __str__(self):
        return f'{self.user.username} - {self.movie.title} - ' \
               f'{self.review_type} - {self.pk}'


class UserReviewSerial(models.Model):
    """
    Contains user serials review. Have ForeignKey on Serial model
    """
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE,
                             default=None)
    serial = models.ForeignKey('Serial', on_delete=models.CASCADE,
                               default=None)
    review_type = models.CharField(max_length=100,
                                   choices=type_of_review)
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=10_000)
    created = models.DateTimeField(auto_now_add=True,
                                   null=True)

    def __str__(self):
        return f'{self.user.username} - {self.serial.serial_name} - ' \
               f'{self.review_type} - {self.pk}'


class UsersReviewLikeDislikeMovie(models.Model):
    """
    Contains like/dislike under movie reviews.
    Have ForeignKey on UserReviewMovie and CustomUser
    """
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE,
                             default=None)

    review = models.ForeignKey('UserReviewMovie', on_delete=models.CASCADE,
                               default=None)
    like_dislike = models.CharField(max_length=100,
                                    choices=like_dislike_review)

    def __str__(self):
        return f'{self.user.username} - {self.review.movie.title} - ' \
               f'{self.like_dislike} - {self.pk}'


class UsersReviewLikeDislikeSerial(models.Model):
    """
    Contains like/dislike under Serial reviews.
    Have ForeignKey on UserReviewSerial and CustomUser
    """
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE,
                             default=None)

    review = models.ForeignKey('UserReviewSerial', on_delete=models.CASCADE,
                               default=None)
    like_dislike = models.CharField(max_length=100,
                                    choices=like_dislike_review)

    def __str__(self):
        return f'{self.user.username} - {self.review.serial.serial_name} - ' \
               f'{self.like_dislike} - {self.pk}'
