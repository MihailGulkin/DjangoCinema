from django import template
from datetime import datetime

register = template.Library()


@register.filter(name='age_calculate')
def age_calculate(date):
    return datetime.now().year - date.year


@register.filter(name='convert_visualize')
def convert_visualize(height: str):
    height = int(height)
    return f'{height // 100},{height % 100}'
