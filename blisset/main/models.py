from django.db import models
from transliterate import translit
from django.utils.safestring import mark_safe
from .data.sizes import SIZES, SIZES_DICT
from colorfield.fields import ColorField

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
class ColorModel(models.Model):
    color = ColorField(default='#000000')
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = "Цвета"


class PhotoModel(models.Model):
    img = models.ImageField(upload_to='media/img/')

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'

    def get_image(self):
        return mark_safe(f"<img width='200px' src='{self.img.url}'>")


class CollectionModel(models.Model):
    name = models.CharField(max_length=100)

    def get_url(self):
        return translit(self.name, language_code='ru', reversed=True).replace(' ', '_').lower()

    def __str__(self):
        return self.name

    def get_img(self):
        # return ClothesModel.objects.filter(collection=self)[0].photos.objets.all[0]
        if len(ClothesModel.objects.filter(collection_id=self.pk)) > 0:
            return ClothesModel.objects.filter(collection_id=self.pk)[0].photos.all()[0].img
        else:
            return ""

        # return self.pk

    class Meta:
        verbose_name = 'Коллекция'
        verbose_name_plural = 'Коллекции'


class ClothesModel(models.Model):
    name = models.CharField(max_length=250)
    collection = models.ForeignKey(CollectionModel, on_delete=models.CASCADE)
    # sizes = models.IntegerField(choices=SIZES_CHOICES)
    sizes = models.CharField(max_length=250, default="")
    photos = models.ManyToManyField(PhotoModel)
    colors = models.ManyToManyField(ColorModel)
    construction = models.TextField()
    features = models.TextField()
    article = models.CharField(max_length=250)
    composition = models.TextField()

    def get_collection_pk(self):
        return self.collection.pk

    def get_sizes(self):
        return [SIZES_DICT[size.replace(' ', '')] for size in self.sizes.split(',') if size.replace(' ', '') in SIZES]

    class Meta:
        verbose_name = 'Одежда'
        verbose_name_plural = 'Одежда'

    def __str__(self):
        return self.name


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
        verbose_name_plural = 'Конфигурация'
