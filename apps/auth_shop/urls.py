from django.contrib import admin
from django.urls import path, include

from .views import LoginView, CreateUserView

app_name = 'auth_shop'


urlpatterns = [
   path('', LoginView.as_view(), name='login'),
   path('create/', CreateUserView.as_view(), name="create"),
]