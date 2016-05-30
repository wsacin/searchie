from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', OldBaseSearchView(), name='base-list'),
    url(r'^(?P<pk>[0-9]+)/$', BaseDetailView.as_view(), name='base-detail'),

    url(r'^create/$', BaseCreateView.as_view(), name='base-create'),
    url(r'^(?P<pk>[0-9]+)/update/$', BaseUpdateView.as_view(), name='base-update'),
    url(r'^(?P<pk>[0-9]+)/delete/$', BaseDeleteView.as_view(), name='base-delete'),
    url(r'^(?P<pk>[0-9]+)/log/$', LogDetailView.as_view(), name='log-detail'),
]
