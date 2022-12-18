from django import template

register = template.Library()

from .. import models


@register.simple_tag
def email():
    try:
        return models.ConfigsModel.objects.get(name='email').value
    except:
        return models.BASE_CONFIGS.get('email')['value']


@register.simple_tag
def instagram():
    try:
        return models.ConfigsModel.objects.get(name='instagram').value
    except:
        return models.BASE_CONFIGS.get('instagram')['value']


@register.simple_tag
def instagram2():
    try:
        return models.ConfigsModel.objects.get(name='instagram2').value
    except:
        return models.BASE_CONFIGS.get('instagram2')['value']


@register.simple_tag
def collections5():
    return models.CollectionModel.objects.all()[:5]
