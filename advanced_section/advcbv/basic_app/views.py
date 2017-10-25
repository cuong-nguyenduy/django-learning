from django.shortcuts import render
from django.views import View
from django.http import HttpResponse


# Create your views here.
class CBView(View):
    def get(self, request):
        return HttpResponse('<h1>Hello, World! Index Page Home with CBView</h1>')
