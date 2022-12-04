from django.db import models
from transliterate import translit


# Create your models here.
class CollectionModel(models.Model):
    name = models.CharField(max_length=100)

    def get_url(self):
        return translit(self.name, language_code='ru', reversed=True).replace(' ', '_').lower()

    def __str__(self):
        return self.name
