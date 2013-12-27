from django import template
from headline.utils import to_relative_time

register = template.Library()

@register.filter(name='relative_time')
def relative_time(value):
    return to_relative_time(value)
