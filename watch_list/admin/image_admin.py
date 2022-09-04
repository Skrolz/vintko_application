from django.contrib import admin
from watch_list.models import Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': (
                'watch',
                'file',
                'description',
                'is_visible',
            )
        }),
        ('Save info', {
            'classes': ('collapse',),
            'fields': ('modified', 'created',),
        }),
    )
    list_display  = (
        'watch',
        'file',
        'is_visible',
    )
    ordering = ['watch',]
    readonly_fields = ('modified', 'created',)
