from rest_framework import serializers
from inventory.models import Demand, DemandRow, Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item


class DemandRowSerializer(serializers.ModelSerializer):
    class Meta:
        model = DemandRow


class DemandSerializer(serializers.ModelSerializer):
    rows = DemandRowSerializer()

    class Meta:
        model = Demand
