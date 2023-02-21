from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views import View


class ViewCart(View):
   def get(self, request):
       return render(request, 'checkout/checkout.html')
