from django import template

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

    # из блог хтмл извлечь все из блог
    # сделать новое приложение блог