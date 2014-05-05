from haystack import indexes
# from haystack.fields import EdgeNgramField
from ils.models import Record, Author, Publisher


class RecordIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    isbn13 = indexes.CharField(model_attr='isbn13', null=True)
    date_of_publication = indexes.DateField(model_attr='date_of_publication', null=True)

    def get_model(self):
        return Record

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return Record.objects.all()


class AuthorIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Author

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return Author.objects.all()


class PublisherIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Publisher

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return Publisher.objects.all()