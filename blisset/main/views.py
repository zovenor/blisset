from django.shortcuts import render, redirect
from django.views import View
from . import models


# Create your views here.
class mainPage(View):
    def get(self, request):
        data = {
            'configs': models.ConfigsModel.objects.all(),
            'slider1': models.MainPageSlider1Model.objects.all(),
            'slider2': models.MainPageSlider2Model.objects.all()
        }
        return render(request, 'main/mainpage.html', data)

    def post(self, request):
        return redirect('/')


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

    def post(self, request):
        return mainPage.post(request)


class CollectionsPage(View):
    def get(self, request):
        collections = models.CollectionModel.objects.all()
        data = {
            'collections': collections
        }
        return render(request, 'main/collections.html', data)

    def post(self, request):
        return mainPage.post(request)


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

    def post(self, request):
        return mainPage.post(request)


class ContactUsPage(View):
    def get(self, request):
        return render(request, 'main/contact_us.html')

    def post(self, request):
        return mainPage.post(request)


class AboutUsPage(View):
    def get(self, request):
        return render(request, 'main/about_us.html')

    def post(self, request):
        return mainPage.post(request)


class GiftCertificatePage(View):
    def get(self, request):
        return render(request, 'main/gift_certificate.html')

    def post(self, request):
        return mainPage.post(request)


class SizeGuidePage(View):
    def get(self, request):
        return render(request, 'main/size_guide.html')

    def post(self, request):
        return mainPage.post(request)


class CareGuidePage(View):
    def get(self, request):
        return render(request, 'main/care_guide.html')

    def post(self, request):
        return mainPage.post(request)
