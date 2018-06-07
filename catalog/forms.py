from django import forms

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime #for checking renewal date range.


class InputLoginForm(forms.Form):
    field = forms.CharField(widget=forms.TextInput(attrs={'class': 'test'}))


class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file',
        help_text='max. 42 megabytes'
    )
