from django.urls import path

from .views import base


urlpatterns = [
    path('<slug:slug>', base, name='sub'),
    path('', base, name='base'),
]