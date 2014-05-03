from haystack import indexes
from ils.models import Record

class RecordIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    isbn13 = indexes.CharField(model_attr='isbn13', null=True)
    date_of_publication = indexes.DateField(model_attr='date_of_publication', null=True)

    def get_model(self):
        return Record



