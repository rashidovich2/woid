# coding: utf-8

from django import template

register = template.Library()


@register.filter('startswith')
def startswith(text, starts):
    starts = f'/{starts}/'
    return text.startswith(starts) if isinstance(text, str) else False
