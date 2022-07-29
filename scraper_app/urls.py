from django.urls import path
from .views import Home_View, add_items

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   
    path('', Home_View.as_view(), name="home"),
    path('add_items/<int:indice_id>', add_items, name="add_items"),

]