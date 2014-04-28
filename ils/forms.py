from django import forms
from app.libr import KOModelForm
from models import Record, Transaction


class RecordForm(forms.ModelForm):
    class Meta:
        model = Record


class OutgoingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(OutgoingForm, self).__init__(*args, **kwargs)
        self.fields['user'].label = 'Patron'
        self.fields['record'].empty_label = None
        self.fields['user'].empty_label = None

    class Meta:
        model = Transaction
        exclude = ['fine_paid', 'fine_per_day', 'returned', 'return_date']