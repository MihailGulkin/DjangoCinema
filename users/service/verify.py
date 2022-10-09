from ..models import CustomUser


def verify_user(username):
    user = CustomUser.objects.get(username=username)
    return user.is_verified

