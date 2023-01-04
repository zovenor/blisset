from django import template

register = template.Library()

from .. import models


@register.simple_tag
def info_orders():
    return models.InformationOfOrdersModel.objects.all()
