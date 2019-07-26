from django.contrib import admin

# Register your models here.

from .models import Artikel, VocabsIndo

class ArtikelAdmin(admin.ModelAdmin):
    list_display = ['id', 'judul', 'kategori', 'tanggal',]  
    list_display_links = ['judul']

class VocabsIndoAdmin(admin.ModelAdmin):
    list_display = ['id', 'indo', 'arti', 'related', 'sinonim']
    list_display_links = ['indo']

admin.site.register(Artikel, ArtikelAdmin)
admin.site.register(VocabsIndo, VocabsIndoAdmin)
