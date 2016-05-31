import datetime
from haystack import indexes
from .models import Base, Log


class BaseIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    value = indexes.CharField(model_attr='value')

    def get_model(self):
        return Base

    def index_queryset(self, using=None):
        return self.get_model().objects.all()


class LogIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    timestamp = indexes.DateTimeField(model_attr='timestamp')
    operation = indexes.CharField(model_attr='operation')

    def get_model(self):
        return Log

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
