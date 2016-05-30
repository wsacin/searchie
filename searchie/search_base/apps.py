from django.apps import AppConfig


class SearchBaseConfig(AppConfig):
    name = 'search_base'
    verbose_name = 'Search Base Application'

    def ready(self):
        from . import signals