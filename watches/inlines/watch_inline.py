from django.contrib import admin
from watches.models import Watch


class WatchInline(admin.TabularInline):
    fields = ('year', 'model', 'reference_number', 'movement_type', 'case_material', 'is_visible',)
    extra = 1
    model = Watch
    ordering = ['year', 'model',]
    show_change_link = True
