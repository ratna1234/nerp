from rest_framework import serializers
from models import Book, Record, Author, Publisher


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book


class RecordSerializer(serializers.ModelSerializer):
    book = BookSerializer()

    class Meta:
        model = Record


        # class AccountSerializer(serializers.ModelSerializer):
        #     name = serializers.Field(source='name')
        #
        #     class Meta:
        #         model = Account
        #
        #
        # class ReceiptRowSerializer(serializers.ModelSerializer):
        #     tax_scheme_id = serializers.Field(source='tax_scheme.id')
        #     budget_head_id = serializers.Field(source='budget_head.id')
        #     account_id = serializers.Field(source='account.id')
        #     activity_id = serializers.Field(source='activity.id')
        #
        #     class Meta:
        #         model = ReceiptRow
        #         exclude = ['tax_scheme', 'budget_head', 'account', 'activity']
        #
        #
        # class ReceiptSerializer(serializers.ModelSerializer):
        #     rows = ReceiptRowSerializer()
        #
        #     class Meta:
        #         model = Receipt