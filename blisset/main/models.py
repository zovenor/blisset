from django.db import models
from transliterate import translit

BASE_CONFIGS = {
    'email': {
        'str': 'Почта',
        'value': 'info@blisset.by'
    },
    'instagram': {
        'str': 'Инстаграм',
        'value': 'blissetofficial'
    },
    'instagram2': {
        'str': 'Инстаграм2',
        'value': 'blissetweddig'
    }
}


# Create your models here.
class CollectionModel(models.Model):
    name = models.CharField(max_length=100)

    def get_url(self):
        return translit(self.name, language_code='ru', reversed=True).replace(' ', '_').lower()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Коллекции'


class ConfigsModel(models.Model):
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=100)

    def __str__(self):
        if self.name in BASE_CONFIGS:
            return BASE_CONFIGS[self.name]['str']
        else:
            return self.name

    class Meta:
        verbose_name = 'Конфигурация'
