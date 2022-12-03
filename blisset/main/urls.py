from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainPage.as_view())
]
