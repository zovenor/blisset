from django.shortcuts import render
from django.views import View


# Create your views here.
class mainPage(View):
    def get(self, request):
        data = {}
        return render(request, 'main/mainpage.html', data)
