from django.views import View
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.urls import reverse, reverse_lazy

class Home(View):
    def get(self, request):
        return render(request, "index.html")
    
class Game(View):
    def get(self, request):
        ctxt = {
            "var":"hello world"
        }
        return render(request, "game.html",context=ctxt)