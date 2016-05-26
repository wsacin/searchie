from datetime import timezone, datetime

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView

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
        print(Base.pk)
        print('\n\n\n\n')
        context = super(BaseDetailView, self).get_context_data(**kwargs)
        context['now'] = datetime.now()
        return context
