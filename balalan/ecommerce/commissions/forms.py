from dashboard.models import Commissions
from django import forms
from django.forms import ModelForm
from django.core.validators import FileExtensionValidator


class CommissionForm(forms.ModelForm):
	class Meta:
		model = Commissions
		fields = ('ae_product','product')		

class ImportForm(forms.Form):
    import_file = forms.FileField(allow_empty_file=False, validators=[
                                  FileExtensionValidator(allowed_extensions=['csv', 'xls', 'xlsx'])], label="")
