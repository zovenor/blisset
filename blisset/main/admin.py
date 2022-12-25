from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.CollectionModel)
admin.site.register(models.ConfigsModel)


# admin.site.register(models.ClothesModel)


class ImagesInline(admin.TabularInline):
    model = models.ClothesModel.photos.through
    extra = 1


class ColorsInline(admin.TabularInline):
    model = models.ClothesModel.colors.through
    extra = 1


@admin.register(models.PhotoModel)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['pk', 'get_image']

    readonly_fields = ['get_image']


@admin.register(models.ClothesModel)
class ClothesAdmin(admin.ModelAdmin):
    inlines = [
        ImagesInline,
        ColorsInline
    ]
    exclude = ('photos', 'colors')
    list_filter = ('collection', 'colors')


@admin.register(models.ColorModel)
class ColorAdmin(admin.ModelAdmin):
    model = models.ColorModel
