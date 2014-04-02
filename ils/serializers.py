from rest_framework import serializers
from models import Book, Record, Author, Publisher, Subject


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher


class BookSerializer(serializers.ModelSerializer):
    # authors = AuthorSerializer()
    # author_id = serializers.Field(source='author.id')

    class Meta:
        model = Book
        exclude = ['id', 'slug']


class RecordSerializer(serializers.ModelSerializer):
    # publisher = PublisherSerializer()
    book = BookSerializer()
    publisher_id = serializers.Field(source='publisher.id')

    class Meta:
        model = Record
        exclude = ['slug', 'publisher']


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