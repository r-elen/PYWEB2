from django.urls import path
from .views import ViewCart, ViewBlogSingle

app_name = 'blog'

urlpatterns = [
   path('', ViewCart.as_view(), name='blog'),
   path('', ViewBlogSingle.as_view(), name='blog-single'),
]
