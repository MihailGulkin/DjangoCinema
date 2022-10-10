from django import template
from web.models import UserReviewMovie
from web.models import UserReviewSerial

register = template.Library()


def calculate_review_user(model_review, user):
    return model_review.objects.filter(user=user).count()


@register.filter(name='calculate_review_user_film')
def calculate_review_user_film(user):
    return calculate_review_user(UserReviewMovie, user)


@register.filter(name='calculate_review_user_serial')
def calculate_review_user_serial(user):
    return calculate_review_user(UserReviewSerial, user)
