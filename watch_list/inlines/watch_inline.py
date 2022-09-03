from django.contrib import admin
from watch_list.models import Watch


class WatchInline(admin.TabularInline):
    fields = ('year', 'model', 'reference_number', 'movement_type', 'case_material', 'is_visible',)
    extra = 1
    model = Watch
