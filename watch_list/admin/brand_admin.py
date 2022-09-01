from django.contrib import admin
from watch_list.models import Brand
from watch_list.inlines import WatchInline


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    fields = ('name', 'country',)
    inlines = [WatchInline]
    list_display  = ('name', 'country',)
