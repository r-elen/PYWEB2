from django.shortcuts import render

# Create your views here.
from datetime import datetime

from django.views import View
from .forms import CustomUserCreationForm

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from apps.cart_shop.models import CartUser


class LoginView(View):
   def get(self, request):
       return render(request, "login.html")

   def post(self, request):
       form = AuthenticationForm(data=request.POST)
       if form.is_valid():
           username = form.cleaned_data.get('username')
           password = form.cleaned_data.get('password')
           user = authenticate(username=username, password=password)
           if user is not None:
               login(request, user)
               print(user)
               return redirect('home:index')
       return redirect('auth_shop:login')


class CreateUserView(View):
   def get(self, request):
       return render(request, "login.html")

   def post(self, request):
       form = CustomUserCreationForm(data=request.POST)
       if form.is_valid():
           username = form.cleaned_data.get('username')
           email = form.cleaned_data.get('email')
           password = form.cleaned_data.get('password1')
           user = User.objects.create_user(username=username, email=email, password=password)
           user.save()
           cart = CartUser(user=user)
           cart.save()
           login(request, user)
           return redirect('home:index')
       return redirect('auth_shop:login')

