from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from webowl import urls

urlpatterns = [
    path('', include('webowl.urls')),
]
