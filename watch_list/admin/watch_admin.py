from django.contrib import admin
from watch_list.models import Watch
from watch_list.inlines import ImageInline, ValueInline


@admin.register(Watch)
class WatchAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': (
                ('brand',
                'model',
                'movement_type',),
                'year',
                ('case_material',
                'band_material',),
                ('case_width',
                'case_thickness',
                'lug_width',
                'lug_to_lug',),
                'description',
                'is_visible',
            )
        }),
        ('Save Info', {
            'classes': ('collapse',),
            'fields': ('modified', 'created'),
        }),
    )
    inlines = [ValueInline, ImageInline,]
    list_display  = (
        'brand',
        'model',
        'year',
        'case_material',
        'band_material',
        'case_width',
        'is_visible',
    )
    ordering = ['brand', 'model',]
    readonly_fields = ('modified', 'created',)
