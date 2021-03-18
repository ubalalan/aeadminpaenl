from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


# Create your models here.

class Currents(models.Model):
    name = models.CharField(max_length=200, null=True,
                            verbose_name="Cari Adı")
    date_added = models.DateTimeField(
        default=datetime.now, blank=True, verbose_name="Oluşturulma Tarihi")
  

    def __str__(self):
        return self.name