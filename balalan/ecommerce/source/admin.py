from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.

@admin.register(Source)
class SourceAdmin(ImportExportModelAdmin):
    list_display=(
        'product_sku',
        'name',
        'price',
        'discount_price',
        'quantity', 
        'link',
        'marketplace'

    )
    search_fields = ('name',)