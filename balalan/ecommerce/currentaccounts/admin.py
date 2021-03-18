from django.contrib import admin
from .models import Currents
from import_export.admin import ImportExportModelAdmin

# Register your models here.


@admin.register(Currents)
class CurrentsAdmin(ImportExportModelAdmin):
    list_display = (
        'name',
        'date_added'
    )

    search_fields = ('name',)