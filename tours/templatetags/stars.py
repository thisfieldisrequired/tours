from django import template


register = template.Library()

@register.simple_tag
def stars(number):
    return '★' * int(number)
