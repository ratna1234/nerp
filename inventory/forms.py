from django import forms


class CategoryForm(forms.Form):
    code = forms.CharField(max_length=10, required=False)
    name = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea, required=False)


class ItemForm(forms.Form):
    code = forms.CharField(max_length=10, required=False)
    name = forms.CharField(max_length=100)
    price = forms.FloatField(required=False)
    category = forms.ChoiceField(required=False)
    description = forms.CharField(widget=forms.Textarea)
