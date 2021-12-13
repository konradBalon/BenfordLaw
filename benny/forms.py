from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from benny.models import Document


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document',)


