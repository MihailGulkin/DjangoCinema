from django import template

register = template.Library()


@register.filter(name='add_css_color')
def add_css_color(review_type):
    color = {'Positive': 'blue_color_review_type',
             'Neutral': 'gray_color_review_type',
             'Negative': 'red_color_review_type'}
    return color.get(review_type, 'Negative')

