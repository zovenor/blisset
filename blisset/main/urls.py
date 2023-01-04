from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainPage.as_view()),
    path('collections', views.CollectionsPage.as_view()),
    path('collections/<str:collection_name>', views.CollectionPage.as_view()),
    path('clothes/<str:id_>', views.ClothesPage.as_view()),
    path('contact_us', views.ContactUsPage.as_view()),
    path('about_us', views.AboutUsPage.as_view()),
    path('gift_certificate', views.GiftCertificatePage.as_view()),
    path('size_guide', views.SizeGuidePage.as_view()),
    path('care_guide', views.CareGuidePage.as_view()),
    path('info/<str:id_>', views.InfoPage.as_view())
]
