from django.contrib import admin

from .models import Base, Log

admin.site.register(Base)
admin.site.register(Log)
