from django.contrib import admin
from .models import Marketplaces
from import_export.admin import ImportExportModelAdmin


# Register your models here.
@admin.register(Marketplaces)
class MarketplacesAdmin(ImportExportModelAdmin):
    list_display = (
        'name',
        'url', 
        'current_price', 
        'old_price',
        'price_difference', 
        'updated', 
        'created'
    )

    search_fields = ('name', 'current_price')