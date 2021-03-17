from dashboard.models import Source
from django import forms
from django.core.validators import FileExtensionValidator


class SourceForm(forms.ModelForm):
	class Meta:
		model = Source
		fields = ('product_sku','name','price','discount_price','quantity','link','marketplace')
		
class ImportForm(forms.Form):
    import_file = forms.FileField(allow_empty_file=False, validators=[
                                  FileExtensionValidator(allowed_extensions=['csv', 'xls', 'xlsx'])], label="")
