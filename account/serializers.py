from rest_framework import serializers
from account.models import Receipt
from core.models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account

class ReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receipt