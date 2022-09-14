from django import template

register = template.Library()


@register.filter(name='for_range')
def for_range(number: int):
    return range(number)
