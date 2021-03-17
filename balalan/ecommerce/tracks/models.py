from django.db import models
from datetime import datetime
import products.models
# Create your models here.

class Track(models.Model):
     sku= models.CharField(max_length=200, null=True,verbose_name="Ürün SKU")
     ae_product=models.ForeignKey(products.models.Product, on_delete=models.SET_NULL, null=True, blank=True,verbose_name="Ürün Bilgisi -AE")
     title = models.CharField(max_length=200, null=True,verbose_name="Ürün Adı")
     price=models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Fiyat")
     discount_price= models.DecimalField(max_digits=7, decimal_places=2,verbose_name="İndirim Fiyatı")
     link = models.CharField(max_length=200, null=True,verbose_name="Link ") 
     date_added = models.DateTimeField(
        default=datetime.now, blank=True, verbose_name="Oluşturulma Tarihi")
     
     def __str__(self):
       return str(self.sku)