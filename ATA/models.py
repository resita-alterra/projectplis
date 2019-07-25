from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class VocabsIndo(models.Model):
    indo = models.CharField(max_length=50)
    arti = models.TextField()
    related = models.TextField()
    sinonim = models.TextField()


class Artikel(models.Model):
    foto = models.CharField(max_length=100)
    judul = models.CharField(max_length=100)
    tanggal = models.DateField()
    isi = models.TextField()
    kategori = models.CharField(max_length=100)

