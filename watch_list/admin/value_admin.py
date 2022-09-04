from django.contrib import admin
from watch_list.models import Value


@admin.register(Value)
class ValueAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': (
                'watch',
                'type',
                'description',
                'amount',
                'date',
            )
        }),
        ('Save Info', {
            'classes': ('collapse',),
            'fields': ('modified', 'created',),
        }),
    )
    list_display  = (
        'watch',
        'type',
        'amount',
        'date',
    )
    ordering = ['-date',]
    readonly_fields = ('modified', 'created',)
