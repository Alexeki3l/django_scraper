from django.db import models
from .utils import get_link

# Create your models here.
class Indice(models.Model):
    name 		= models.CharField(max_length=255)
    count_items	= models.IntegerField(default=0)
    url 		= models.URLField(blank=True)
    created 	= models.DateTimeField(auto_now_add=True)
    updated 	= models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ('-created',)

    def save(self, *args, **kwargs):
        self.url = get_link(self.name)
        super().save(*args, **kwargs)

class Items(models.Model):
    name 		        = models.CharField(max_length=255)
    image		        = models.ImageField()
    current_price 	    = models.FloatField(blank=True)
    old_price 	        = models.FloatField(default=0)
    price_difference    = models.FloatField(default=0)
    trading 	        = models.CharField(max_length=30)
    trading_count 	    = models.IntegerField()
    url 		        = models.URLField()
    indices 	        = models.ForeignKey(Indice, on_delete=models.CASCADE)
    created 	        = models.DateTimeField(auto_now_add=True)
    updated 	        = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created','current_price')

    def __str__(self):
        return str(self.name)

    def image_url(self):
        if self.imagen and hasattr(self.imagen, 'url'):
            return self.imagen.url

    def save(self, *args, **kwargs):
        self.url = get_link(self.name)
        super().save(*args, **kwargs)


    

    