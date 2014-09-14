from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def currency(amount, currency_format="{0}"):
    return mark_safe(currency_format.format(
        "{0:.2f}".format(amount)
    ))