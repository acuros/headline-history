import re

from django import template
from django.utils.safestring import mark_safe
from headline.utils import to_relative_time

register = template.Library()

@register.filter(name='relative_time')
def relative_time(value):
    return to_relative_time(value)

@register.filter(name='emphasize')
def emphasize(value, query):
    pattern = re.escape(query)
    repl = ur'<span class="red">\g<0></span>'
    emphasized = re.sub(pattern, repl, value, flags=re.IGNORECASE)
    return mark_safe(emphasized)

