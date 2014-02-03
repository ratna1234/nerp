from rest_framework import serializers
from account.models import Receipt, ReceiptRow
from core.models import Account


class AccountSerializer(serializers.ModelSerializer):
    name = serializers.Field(source='name')

    class Meta:
        model = Account


class ReceiptRowSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReceiptRow


class ReceiptSerializer(serializers.ModelSerializer):
    rows = ReceiptRowSerializer()

    class Meta:
        model = Receipt