from django.conf.urls import url
from haystack.views import SearchView
from .views import BaseListView, BaseDetailView

urlpatterns = [
    url(r'^$', BaseListView.as_view(), name='base-list'),
    url(r'^search/', SearchView(), name='haystack_search'),
    url(r'^(?P<pk>[0-9]+)/$', BaseDetailView.as_view(), name='base-detail'),
]
