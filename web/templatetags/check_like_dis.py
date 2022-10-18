from django import template
from web.models import UsersReviewLikeDislikeMovie, \
    UsersReviewLikeDislikeSerial

register = template.Library()


@register.simple_tag(name='like_dislike_review_movie')
def movie_checker_l_d(request, review, choose):
    """
    Have movie review like/dislike
    :param request:
    :param review:
    :param choose:
    :return:
    """
    if request.user.is_authenticated:
        return UsersReviewLikeDislikeMovie.objects.filter(
            user=request.user,
            like_dislike=choose,
            review=review).exists()
    return False


@register.simple_tag(name='calculate_l_d_movie')
def calculate_movie_l_d(review):
    """
    Calculate how many like/dislike movie review have
    :param review:
    :return:
    """
    _obj = UsersReviewLikeDislikeMovie.objects.filter(
        review=review
    )

    _result = {'Like': 0,
               'Dislike': 0}
    for ele in _obj:
        _result[ele.like_dislike] += 1
    return _result


@register.simple_tag(name='like_dislike_review_serial')
def serial_checker_l_d(request, review, choose):
    """
   Calculate how many like/dislike serial review have
   :param review:
   :return:
   """
    if request.user.is_authenticated:
        return UsersReviewLikeDislikeSerial.objects.filter(
            user=request.user,
            like_dislike=choose,
            review=review).exists()
    return False


@register.simple_tag(name='calculate_l_d_serial')
def calculate_serial_l_d(review):
    """
   Calculate how many like/dislike serial review have
   :param review:
   :return:
   """
    _obj = UsersReviewLikeDislikeSerial.objects.filter(
        review=review
    )
    _result = {'Like': 0,
               'Dislike': 0}
    for ele in _obj:
        _result[ele.like_dislike] += 1
    return _result
