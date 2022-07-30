from itertools import count
from django.shortcuts import render, redirect
from .models import Indice, Items
from .utils import get_items

from django.views.generic import ListView, DetailView
# Create your views here.


def add_items(request, indice_id):
    indice = Indice.objects.filter(id = indice_id).first()
    product_names, ratings, ratings_count, prices, product_urls, images = get_items(indice.url)
    list_items = []
    for i in range(3):
        
        articulo = Items(
            name = product_names[i],
            current_price = prices[i],
            rating = ratings[i],
            image = images[i],
            rating_count = ratings_count[i],
            url = product_urls[i],
            indices = indice
        )
        list_items.append(articulo)
    Items.objects.bulk_create(list_items)
    Indice.objects.filter(id = indice_id).update(count_items = len(list_items))
    return redirect('home')

def show_items(request, indice_id):
    indice = Indice.objects.filter(id = indice_id).first()
    items = Items.objects.filter(indices_id = indice_id)
    return render(request, "scraper_app/details_search.html",{"items":items })
class Home_View(ListView):
    model = Indice
    template_name = 'scraper_app/home.html'
    context_object_name = 'indices'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     indice = Indice.objects.filter(id = kwargs['indices']).first()
    #     context['count_items'] = Items.objects.filter(indice = indice)



