from django import template
from web.models import UserReviewMovie
from web.models import UserReviewSerial

register = template.Library()


def calculate_review_user(model_review, user):
    """
    Return count of user review
    :param model_review:
    :param user:
    :return:
    """
    return model_review.objects.filter(user=user).count()


@register.filter(name='calculate_review_user_film')
def calculate_review_user_film(user):
    """
    Return count of user review film
    :param user:
    :return:
    """
    return calculate_review_user(UserReviewMovie, user)


@register.filter(name='calculate_review_user_serial')
def calculate_review_user_serial(user):
    """
    Return count of user review film
    :param user:
    :return:
    """
    return calculate_review_user(UserReviewSerial, user)
