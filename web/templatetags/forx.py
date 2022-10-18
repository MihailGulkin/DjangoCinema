from django import template

register = template.Library()


@register.filter(name='for_range')
def for_range(number: int):
    """for range in templates"""
    return range(number)
