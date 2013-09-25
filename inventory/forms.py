from mptt.forms import TreeNodeChoiceField

from app.lib import KOModelForm
from models import Item, Category, Demand, Party, PurchaseOrder


class ItemForm(KOModelForm):
    category = TreeNodeChoiceField(queryset=Category.objects.all(), required=False)

    class Meta:
        model = Item
        exclude = ['account']


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
