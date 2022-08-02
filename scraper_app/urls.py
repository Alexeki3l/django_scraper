from django.urls import path
from .views import home_view, add_items, show_items, DeleteIndiceView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   
    path('', home_view, name="home"),
    path('add_items/<int:indice_id>', add_items, name="add_items"),
    path('show_items/<int:indice_id>', show_items, name="show_items"),
    path('delete_indice/<pk>/', DeleteIndiceView.as_view(), name="delete_indice"),

]