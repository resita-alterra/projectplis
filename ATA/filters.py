import django_filters
from .models import Artikel



class ArtikelFilter(django_filters.FilterSet):
    class Meta:
        model = Artikel
        fields = {
            'kategori': ['exact'],
        }