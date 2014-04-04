from django import forms
from app.libr import KOModelForm
from models import Record


class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
