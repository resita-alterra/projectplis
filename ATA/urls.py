from django.contrib import admin
from django.urls import path
from django_filters.views import FilterView
from django_filters.views import object_filter

from . import views

urlpatterns = [
    path('', views.order3, name='home'),
    path('artikel/<int:blog_id>/', views.artikel_detail, name='artikel_detail'),
    path('kategori', views.artikel_kategori, name='artikel_kategori')
]
