from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin


@admin.register(Commission)
class CommissionAdmin(ImportExportModelAdmin):
    list_display = (
        'ae_product',
'track_product'

        )