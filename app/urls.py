
from django.contrib import admin
from django.urls import include, path

from .views import *

urlpatterns = [
    path('number/', number, name="number"),
    path('', base, name="base"),
    path('tarif/', tarif, name="tarif"),
    path('kyzmat/', kyzmat, name="kyzmat"),
    path('about', about, name="about"),

]
