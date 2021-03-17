from django.db import models
from .utils import get_link_data

# Create your models here.
class Marketplaces(models.Model):
    name = models.CharField(max_length=220, blank=True ,verbose_name="Ürün Adı")
    url = models.URLField(verbose_name="Ürün Linki")
    current_price = models.FloatField(blank=True,verbose_name="Yeni Fiyat")
    old_price = models.FloatField(default=0,verbose_name="Eski Fiyat")
    price_difference = models.FloatField(default=0,verbose_name="Fiyat Farkı")
    updated = models.DateTimeField(auto_now=True,verbose_name="Günceleme Tarihi")
    created = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturma Tarihi")

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ('price_difference', '-created')

    def save(self, *args, **kwargs):
        name, price = get_link_data(self.url)
        old_price = self.current_price
        if self.current_price:
            if price != old_price:
                diff = price - old_price
                self.price_difference = round(diff, 2)
                self.old_price = old_price
        else:
            self.old_price = 0
            self.price_difference = 0
        
        self.name = name
        self.current_price = price
        
        super().save(*args, **kwargs)  