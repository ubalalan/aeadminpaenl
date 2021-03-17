from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.

@admin.register(Track)
class TrackAdmin(ImportExportModelAdmin):
    list_display=(
        'sku',
        'title', 
        'ae_product',
        'link',
        'price',
        'discount_price',
        'date_added'

    )
    search_fields = ('name',)
