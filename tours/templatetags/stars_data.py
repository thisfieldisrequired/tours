from django import template


register = template.Library()

@register.simple_tag
def stars_data(number):
    return '★' * int(number)
