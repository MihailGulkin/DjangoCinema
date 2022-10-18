from django import template
import time

register = template.Library()


@register.filter(name='hours_convertor')
def hours_conv(min_time: int):
    """Min to hour"""
    return time.strftime('%H:%M', time.gmtime(min_time * 60))
