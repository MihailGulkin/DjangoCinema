from django.core.mail import send_mail
from django.conf import settings


def send_first_verify_email(request, username, user_email) -> None:
    """
    Send first verification email with verify link
    :param request:
    :param username:
    :param user_email:
    :return:
    """
    send_mail(
        f'Hello, {username}. Verify your NovaFilm account.',
        'Follow this link to verify your account: '
        f'{request.build_absolute_uri("/")}verify/{username}',
        settings.EMAIL_HOST_USER,
        [user_email],
        fail_silently=False,
    )


def send_already_verified_email(username, user_email) -> None:
    """
    Send second verification email with confirm message
    :param username:
    :param user_email:
    :return:
    """
    send_mail(
        f'Hello, {username}. You already verified you account',
        'Thank you for choosing our service',
        settings.EMAIL_HOST_USER,
        [user_email],
        fail_silently=False,
    )
