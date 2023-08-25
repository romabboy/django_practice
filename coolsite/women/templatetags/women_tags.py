from django import template
from women.models import *

register = template.Library()


def get_categories(filter=None):
    if not filter:
        result = Category.objects.all()
    else:
        result = Category.objects.filter(pk=filter)

    return result


@register.inclusion_tag('women/list_categories.html')
def show_categories(sort=None, cat_selected=0):
    cats = Category.objects.all()
    if not sort:
        cats = Category.objects.all()
    else:
        cats = Category.objects.order_by(sort)

    return {'cats': cats, 'cat_selected': cat_selected}


@register.inclusion_tag('women/list_menu.html')
def get_menu():
    menu = [{'title': 'About site', 'url_name': 'women:about'},
            {'title': 'Add article', 'url_name': 'women:add_page'},
            {'title': 'Feedback', 'url_name': 'women:contact'},
            {'title': 'Log in', 'url_name': 'women:login'}]

    return {'menu': menu}

register.simple_tag(get_categories, name='my_own_name')
