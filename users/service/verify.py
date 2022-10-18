from ..models import CustomUser


def verify_user(username):
    """
    Check verify user flag
    :param username:
    :return:
    """
    user = CustomUser.objects.get(username=username)
    return user.is_verified

