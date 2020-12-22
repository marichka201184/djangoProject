from django.urls import path

from .views import pets, owners, index

urlpatterns = [
    path('', index),
    path('pet/', pets),
    path('owner/', owners)
]
