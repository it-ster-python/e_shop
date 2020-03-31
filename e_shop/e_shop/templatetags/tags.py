from django import template
from django.conf import settings

register = template.Library()


@register.simple_tag
def price_sale(price, sale):
    return "$" + str(round(price * (1-(sale/100)), 2))

@register.filter
def add_percent(value):
    return str(value) + "%"

@register.filter
def add_dollar(value):
    return "$" + str(value)

@register.simple_tag
def media(value):
    return settings.MEDIA_URL + value.name

@register.filter
def add_comment(value):
    return str(value) + " ""Comments"

