from django.urls import path
from .views import ViewCart

app_name = 'checkout'

urlpatterns = [
   path('', ViewCart.as_view(), name='checkout'),
]
