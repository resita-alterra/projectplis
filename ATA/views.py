from django.shortcuts import render
from .models import VocabsIndo, Artikel

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
