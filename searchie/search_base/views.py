from datetime import timezone, datetime

from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView,\
    CreateView, UpdateView, DeleteView

from .models import Base


class BaseListView(ListView):

    model = Base

    def get_context_data(self, **kwargs):
        context = super(BaseListView, self).get_context_data(**kwargs)
        context['now'] = datetime.now()
        return context


class BaseDetailView(DetailView):

    model = Base

    def get_context_data(self, **kwargs):
        context = super(BaseDetailView, self).get_context_data(**kwargs)
        context['now'] = datetime.now()
        return context


class BaseCreateView(CreateView):
    model = Base
    fields = ['value','text']


class BaseUpdateView(UpdateView):
    model = Base
    fields = ['value','text']
    template_name_suffix = '_update_form'


class BaseDeleteView(DeleteView):
    model = Base
    success_url = reverse_lazy('base-list')