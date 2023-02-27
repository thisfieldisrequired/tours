from django import template

register = template.Library()


def get_stars_data(number):
    return '★' * int(number)


register.filter('get_stars_data', get_stars_data)
