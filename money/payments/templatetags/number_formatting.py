from django import template

register = template.Library()

@register.filter
def currency(amount):
    return "{0:.2f}".format(amount)