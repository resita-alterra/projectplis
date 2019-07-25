from django.contrib import admin

# Register your models here.

from .models import Artikel

class ArtikelAdmin(admin.ModelAdmin):
    list_display = ['id', 'judul', 'tanggal']  
    list_display_links = ['judul']


admin.site.register(Artikel, ArtikelAdmin)