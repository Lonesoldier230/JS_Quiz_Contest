from django.views import View
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.urls import reverse, reverse_lazy

class Home(View):
    def get(self, request):
        return HttpResponse("Home page")