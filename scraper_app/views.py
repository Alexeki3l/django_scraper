from itertools import count
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Indice, Items
from .utils import get_items
from .forms import AddIndiceForm

from django.views.generic import ListView, DetailView, DeleteView
# Create your views here.


def add_items(request, indice_id):
    indice = Indice.objects.filter(id = indice_id).first()
    product_names, ratings, ratings_count, prices, product_urls, images = get_items(indice.url)
    if len(product_names)==0:
        error = 'No se ha encontrado ningun articulo para el indice "{0}". Esto es extraño. Revise su conexion a Internet'.format(indice)
        indices = Indice.objects.all()
        return render(request, "scraper_app/home.html",{"error":error, "indices":indices})
    else:
        list_items = []
        for i in range(50):
            try:
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
                
            except:
                
                print("Error en la iteracion {0}. SALTANDO".format(i))
                continue
        
        Items.objects.bulk_create(list_items)
        Indice.objects.filter(id = indice_id).update(count_items = len(list_items))
        return redirect('home')

def show_items(request, indice_id):
    indice = Indice.objects.filter(id = indice_id).first()
    items = Items.objects.filter(indices_id = indice_id)
    return render(request, "scraper_app/details_search.html",{"items":items })

def home_view(request):
    no_discounted = 0
    error = None

    form = AddIndiceForm(request.POST or None)

    if request.method == 'POST':
        try:
            if form.is_valid():
                form.save()
        except AttributeError:
            error = "Ups ...Debe entrar en nombre de lo que quiere buscar"
        except:
            error = "Ups... algo salio mal"

    form = AddIndiceForm()

    indices = Indice.objects.all()

    context = {
        'indices':indices,
        'form':form,
        'error':error
    }
    return render(request, 'scraper_app/home.html', context)
class DeleteIndiceView(DeleteView):
    model = Indice
    template_name = 'scraper_app/confirm_delete.html'
    success_url = reverse_lazy('home')



