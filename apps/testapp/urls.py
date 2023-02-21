from django.urls import path, include

from .views import RandomView


urlpatterns = [
   path('random/', RandomView.as_view()),
]