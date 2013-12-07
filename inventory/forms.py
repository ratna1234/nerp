from django import forms

from app.libr import KOModelForm
from models import Item, Category, Demand, Party, PurchaseOrder, InventoryAccount, Handover, EntryReport


class ItemForm(KOModelForm):
    #category = TreeNodeChoiceField(queryset=Category.objects.all(), required=False)
    account_no = forms.Field(widget=forms.TextInput())
    opening_balance = forms.Field(widget=forms.TextInput(), initial=0)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(ItemForm, self).__init__(*args, **kwargs)
        self.fields['account_no'].initial = InventoryAccount.get_next_account_no()
        if not self.user.in_group('Store Keeper'):
            self.fields['account_no'].widget = forms.HiddenInput()
            self.fields['opening_balance'].widget = forms.HiddenInput()
            self.fields['property_classification_reference_number'].widget = forms.HiddenInput()
        if self.instance.id:
            self.fields['opening_balance'].widget = forms.HiddenInput()

    def clean_account_no(self):
        try:
            existing = InventoryAccount.objects.get(account_no=self.cleaned_data['account_no'])
            if self.instance.id is not existing.id:
                raise forms.ValidationError("The account no. " + str(
                    self.cleaned_data['account_no']) + " is already in use.")
            return self.cleaned_data['account_no']
        except InventoryAccount.DoesNotExist:
            return self.cleaned_data['account_no']

    class Meta:
        model = Item
        exclude = ['account', 'code', 'category']


class CategoryForm(KOModelForm):
    class Meta:
        model = Category

        # def clean(self):
        #     """ This is the form's clean method, not a particular field's clean method """
        #     cleaned_data = self.cleaned_data
        #
        #     name = cleaned_data.get('name')
        #
        #     if Category.objects.filter(name=name, company=self.company).count() > 0:
        #         raise forms.ValidationError("Category name already exists.")
        #
        #     # Always return the full collection of cleaned data.
        #     return cleaned_data


class DemandForm(KOModelForm):
    class Meta:
        model = Demand

        # def clean(self):
        #     import pdb
        #     pdb.set_trace()


class PartyForm(KOModelForm):
    class Meta:
        model = Party


class PurchaseOrderForm(KOModelForm):
    class Meta:
        model = PurchaseOrder


class HandoverForm(KOModelForm):
    class Meta:
        model = Handover


class EntryReportForm(KOModelForm):
    class Meta:
        model = EntryReport