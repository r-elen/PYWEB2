from django.shortcuts import render

# Create your views here.
from django.views import View
from django.http import HttpResponse

from random import random


class RandomView(View):

    def get(self, request):
        html = f"{random()}"
        return HttpResponse(html)