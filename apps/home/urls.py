from django.urls import path

from .views import IndexShopView, ViewAboout, ViewContact, ViewWishlist

app_name = 'home'

urlpatterns = [
   path('', IndexShopView.as_view(), name='index'),
   path('about/', ViewAboout.as_view(), name='about'),
   path('contact/', ViewContact.as_view(), name='contact'),
   # path('', ViewContact.as_view(), name='wishlist'),
]

