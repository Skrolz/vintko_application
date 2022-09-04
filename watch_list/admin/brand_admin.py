from django.contrib import admin
from watch_list.models import Brand
from watch_list.inlines import WatchInline


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('name', 'country',)
        }),
        ('Save info', {
            'classes': ('collapse',),
            'fields': ('modified', 'created',),
        }),
    )
    inlines = [WatchInline]
    list_display  = ('name', 'country',)
    ordering = ['name',]
    readonly_fields = ('modified', 'created',)
