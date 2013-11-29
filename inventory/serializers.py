from rest_framework import serializers
from inventory.models import Demand, DemandRow, Item, Party, PurchaseOrder, PurchaseOrderRow, HandoverRow, Handover


class ItemSerializer(serializers.ModelSerializer):
    account_no = serializers.Field(source='account.account_no')

    class Meta:
        model = Item


class PartySerializer(serializers.ModelSerializer):
    class Meta:
        model = Party


class DemandRowSerializer(serializers.ModelSerializer):
    item_id = serializers.Field(source='item.id')

    class Meta:
        model = DemandRow
        exclude = ['item']


class DemandSerializer(serializers.ModelSerializer):
    rows = DemandRowSerializer()

    class Meta:
        model = Demand


class PurchaseOrderRowSerializer(serializers.ModelSerializer):
    item_id = serializers.Field(source='item.id')

    class Meta:
        model = PurchaseOrderRow


class PurchaseOrderSerializer(serializers.ModelSerializer):
    rows = PurchaseOrderRowSerializer()

    class Meta:
        model = PurchaseOrder


class HandoverRowSerializer(serializers.ModelSerializer):
    class Meta:
        model = HandoverRow

class HandoverSerializer(serializers.ModelSerializer):
    rows = HandoverRowSerializer()
    class Meta:
        model = Handover
