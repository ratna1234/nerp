from rest_framework import serializers
from inventory.models import Demand, DemandRow, Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item


class DemandRowSerializer(serializers.ModelSerializer):
    item_id = serializers.Field(source='item.id')

    class Meta:
        model = DemandRow
        exclude = ['item']


class DemandSerializer(serializers.ModelSerializer):
    rows = DemandRowSerializer()

    class Meta:
        model = Demand
