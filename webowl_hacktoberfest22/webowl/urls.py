from urllib.parse import urlparse
from django import urls
from django.urls import URLPattern, path
from webowl import views

urlpatterns  =[
    path('', views.red, name="red"),
    path('home/', views.home, name="home"),
]