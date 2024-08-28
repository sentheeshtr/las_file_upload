from django import forms
from .models import LasFile

class LasFileForm(forms.ModelForm):
    class Meta:
        model = LasFile
        fields = ['file']
