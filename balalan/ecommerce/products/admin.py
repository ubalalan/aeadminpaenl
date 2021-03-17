from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.

@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    list_display = (
        'product_id',
        'name',
        'price',
        'quantity'
    )

    search_fields = ('name',)
"""
@admin.register(Suply)
class SuplyAdmin(ImportExportModelAdmin):
    list_display = (
    'aeproduct_id',
    'name', 
    'price', 
    'sku', 
    'pprice'
    )
    search_fields = ('name',)
"""