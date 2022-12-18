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
            ...
        else:
            data = {
                'collection': collection
            }
            return render(request, 'main/collection.html', data)


def find_collection_by_collection_name(collection_name):
    collections = models.CollectionModel.objects.all()
    for collection in collections:
        if collection.get_url() == collection_name:
            return collection
