from django import forms
from .models import *

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['docfile']
        help_texts = {
            'docfile': '42 Mega bytes Max',
        }       