from django import template
from datetime import datetime

register = template.Library()


@register.filter(name='age_calculate')
def age_calculate(date):
    """
    Calculate Director age
    :param date:
    :return:
    """
    return datetime.now().year - date.year


@register.filter(name='convert_visualize')
def convert_visualize(height: str):
    """
    Return normal visualize height in director page
    :param height:
    :return:
    """
    height = int(height)
    return f'{height // 100},{height % 100}'
