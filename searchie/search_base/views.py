from datetime import datetime

from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic import CreateView, UpdateView
from django.views.generic import DeleteView

from .models import Base
from .signals import visualized_base
from .tasks import register_base_deletion


class BaseListView(ListView):
    model = Base

    def get_context_data(self, **kwargs):
        context = super(BaseListView, self).get_context_data(**kwargs)
        context['now'] = datetime.now()
        return context


class BaseDetailView(DetailView):
    model = Base
    template_name = 'search_base/base_detail.html'

    def get_context_data(self, **kwargs):
        context = super(BaseDetailView, self).get_context_data(**kwargs)
        context['now'] = datetime.now()
        return context

    def get(self, request, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)

        visualized_base.send(sender=Base,
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


class BaseDeleteView(DeleteView):
    model = Base
    success_url = reverse_lazy('base-list')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        print("BASE DELETE VIEW")
        print("object.id: " + str(self.object.id))
        register_base_deletion.delay(self.object.id)
        return super(BaseDeleteView, self).delete(request, *args, **kwargs)
