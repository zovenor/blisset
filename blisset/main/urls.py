from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainPage.as_view()),
    path('collections', views.CollectionsPage.as_view()),
    path('collections/<str:collection_name>', views.CollectionPage.as_view()),
    path('clothes/<str:id_>', views.ClothesPage.as_view())
]
