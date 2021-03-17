from django import forms
from django.forms import ModelForm
from django.core.validators import FileExtensionValidator
from .models import Marketplaces

class AddLinkForm(forms.ModelForm):
    class Meta:
        model = Marketplaces
        fields = ('url', )


		
class ImportForm(forms.Form):
    import_file = forms.FileField(allow_empty_file=False, validators=[
                                  FileExtensionValidator(allowed_extensions=['csv', 'xls', 'xlsx'])], label="")