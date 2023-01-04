from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.CollectionModel)


class ImagesInline(admin.TabularInline):
    model = models.ClothesModel.photos.through
    extra = 1


class ColorsInline(admin.TabularInline):
    model = models.ClothesModel.colors.through
    extra = 1


class SizesInline(admin.TabularInline):
    model = models.ClothesModel.sizes.through
    extra = 1


@admin.register(models.PhotoModel)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['pk', 'get_image']

    readonly_fields = ['get_image']


@admin.register(models.ClothesModel)
class ClothesAdmin(admin.ModelAdmin):
    inlines = [
        ImagesInline,
        ColorsInline,
        SizesInline
    ]
    exclude = ('photos', 'colors', 'sizes')
    list_filter = ('collection', 'colors')


@admin.register(models.ColorModel)
class ColorAdmin(admin.ModelAdmin):
    model = models.ColorModel


@admin.register(models.MainPageSlider1Model)
class MainPageSlider1Admin(admin.ModelAdmin):
    model = models.MainPageSlider1Model


@admin.register(models.MainPageSlider2Model)
class MainPageSlider1Admin(admin.ModelAdmin):
    model = models.MainPageSlider2Model


@admin.register(models.SizeModel)
class SizesAdmin(admin.ModelAdmin):
    model = models.SizeModel


@admin.register(models.InformationOfOrdersModel)
class InformationOfOrdersAdmin(admin.ModelAdmin):
    model = models.InformationOfOrdersModel
