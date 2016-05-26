import datetime
from haystack import indexes
from .models import Base, Log


class BaseIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    value = indexes.CharField(model_attr='value')

    def get_model(self):
        return Base

