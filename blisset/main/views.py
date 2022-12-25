from django.shortcuts import render
from django.views import View
from . import models


# Create your views here.
class mainPage(View):
    def get(self, request):
        data = {
            'configs': models.ConfigsModel.objects.all()
        }
        return render(request, 'main/mainpage.html', data)


class CollectionPage(View):
    def get(self, request, collection_name):
        collection = find_collection_by_collection_name(collection_name)
        if collection is None:
            return render(request, 'main/404.html')
        else:
            data = {
                'clothes': models.ClothesModel.objects.filter(collection=collection),
                'collection': collection
            }
            return render(request, 'main/collection.html', data)


class CollectionsPage(View):
    def get(self, request):
        collections = models.CollectionModel.objects.all()
        data = {
            'collections': collections
        }
        return render(request, 'main/collections.html', data)


def page_not_found_view(request, exception):
    return render(request, 'main/404.html', status=404)


def find_collection_by_collection_name(collection_name):
    collections = models.CollectionModel.objects.all()
    for collection in collections:
        if collection.get_url() == collection_name:
            return collection


class ClothesPage(View):
    def get(self, request, id_):
        clothes = models.ClothesModel.objects.get(pk=id_)

        data = {
            'clothes': clothes
        }

        return render(request, 'main/clothes.html', data)
