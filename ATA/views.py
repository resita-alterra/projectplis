from django.shortcuts import render, get_object_or_404
from .models import VocabsIndo, Artikel
from .filters import ArtikelFilter


def artikel_detail(request, blog_id):
    try:
        artikel = Artikel.objects.get(pk=blog_id)
    except Artikel.DoesNotExist:
        raise Http404('Artikel does not exist')
    return render(request, 'artikel_detail.html', {'artikel': artikel})

def headline(request):
    artikel = Artikel.objects.all()
    return render(request, 'headline.html', {'artikels': artikel})


def order3(request):
        # get the blog posts that are published
        artikel = Artikel.objects.order_by('-tanggal')[0:3]
        # now return the rendered template
        return render(request, 'home.html', {'artikels': artikel})

def artikel_kategori(request):
    f = ArtikelFilter(request.GET, queryset=Artikel.objects.all())
    return render(request, 'artikel_kategori.html', {'filter': f})

# Create your views here.

def search(request):
    if request.method == 'GET':
        ini = request.GET.get('cari')
        if ini is not None:
            try:
                arti = VocabsIndo.objects.get(indo=ini)
                return render(request, 'searchkata.html', {'kata':ini,'arti': arti})
            except:
                return render(request,'searchkata.html')
    return render(request,'search.html')
