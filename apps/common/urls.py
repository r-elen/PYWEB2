from django.contrib import admin
from django.urls import path, include

from .views import CurrentDateView, HelloView, IndexView, LoginView


urlpatterns = [
   path('datetime/', CurrentDateView.as_view()),
   path('hello/', HelloView.as_view()),
   path('', IndexView.as_view()),
   path('login/', LoginView.as_view()),

]
