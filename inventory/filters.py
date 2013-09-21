import django_filters
from inventory.models import InventoryAccount, Item


class InventoryItemFilter(django_filters.FilterSet):
    code = django_filters.CharFilter(lookup_type='icontains')
    name = django_filters.CharFilter(lookup_type='icontains')

    class Meta:
        model = Item


class InventoryAccountFilter(django_filters.FilterSet):
    class Meta:
        model = InventoryAccount