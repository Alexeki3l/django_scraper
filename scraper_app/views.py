from django.shortcuts import render, redirect
from .models import Indice, Items
from .utils import get_items

from django.views.generic import ListView
# Create your views here.


def add_items(request, indice_id):
    indice = Indice.objects.filter(id = indice_id).first()
    product_names, ratings, ratings_count, prices, product_urls = get_items(indice.url)
    count = len(product_names)-1
    print(count)
    indice = Indice.objects.get(id = indice_id)
    indice.delete()
    print("eliminado")
    # while count > 0:
        
    #     articulo = Items(
    #         name = product_names[count],
    #         current_price = prices[count],
    #         rating = ratings[count],
    #         rating_count = ratings_count[count],
    #         url = product_urls[count],
    #         indices = indice
    #     )
    #     articulo.save()
    #     count-=0
    return redirect('home')

class Home_View(ListView):
    model = Indice
    template_name = 'scraper_app/home.html'
    context_object_name = 'indices'

