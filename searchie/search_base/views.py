from datetime import datetime

from django.core.paginator import Paginator
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic import CreateView, UpdateView
from django.views.generic import DeleteView
from haystack.forms import SearchForm
from haystack.generic_views import SearchView
from haystack.query import EmptySearchQuerySet, SearchQuerySet
from haystack.utils.app_loading import haystack_get_model
from haystack.views import SearchView as OldSearchView

from .models import Base, Log
from .signals import visualised_base_signal, updated_base_signal
from .tasks import register_base_deletion


class BaseListView(ListView):
    model = Base
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super(BaseListView, self).get_context_data(**kwargs)
        context['now'] = datetime.now()
        return context


class LogListView(ListView):
    model = Log
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super(LogListView, self).get_context_data(**kwargs)
        return context


class BaseDetailView(DetailView):
    model = Base
    template_name_suffix = '_detail'

    def get_context_data(self, **kwargs):
        context = super(BaseDetailView, self).get_context_data(**kwargs)
        context['now'] = datetime.now()
        return context

    def get(self, request, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)

        visualised_base_signal.send(sender=Base,
                                    instance=self.object)

        return self.render_to_response(context)


class BaseCreateView(CreateView):
    model = Base
    fields = ['value', 'text']
    template_name_suffix = '_form'
    success_url = reverse_lazy('base-list')


class BaseUpdateView(UpdateView):
    model = Base
    fields = ['value', 'text']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('base-list')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        new_data = {'value': request.POST['value'],
                    'text': request.POST['text']}

        updated_base_signal.send(sender=Base,
                                 instance=self.object,
                                 new_data=new_data)
        return super(BaseUpdateView, self).post(request, *args, **kwargs)


class BaseDeleteView(DeleteView):
    model = Base
    success_url = reverse_lazy('base-list')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        register_base_deletion.delay(self.object.id,
                                     self.object.value,
                                     self.object.text)
        return super(BaseDeleteView, self).delete(request, *args, **kwargs)


class LogDetailView(DetailView):
    model = Log
    template_name_suffix = '_detail'

    def get_context_data(self, **kwargs):
        context = super(LogDetailView, self).get_context_data(**kwargs)
        context['now'] = datetime.now()
        return context


class BaseSearchView(SearchView):
    template_name = 'search_base/base_list.html'
    form_class = SearchForm
    paginate_by = 20

    def get_queryset(self):
        queryset = super(BaseSearchView, self).get_queryset()
        return queryset.all()

    def get_context_data(self, *args, **kwargs):
        context = super(BaseSearchView, self).get_context_data(*args, **kwargs)
        paginator = Paginator(Base.objects.all(),20)
        context['object_list'] = paginator.page(1)
        return context


class OldBaseSearchView(OldSearchView):
    # TODO: Change to newer SearchView
    template = 'search/base_search.html'

    def extra_context(self):
        paginator = Paginator(Base.objects.all(), 500)

        return {'object_list': paginator.page(1)}


class OldLogSearchView(OldSearchView):
    # TODO: Change to newer SearchView
    template = 'search/log_search.html'

    def extra_context(self):
        paginator = Paginator(Log.objects.all(), 500)

        return {'object_list': paginator.page(1)}
