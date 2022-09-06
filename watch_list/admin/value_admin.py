from django.contrib import admin
from watch_list.models import Value


@admin.register(Value)
class ValueAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': (
                'type',
                ('amount',
                'is_debit',),
                'date',
                'description',
                'watch',
            )
        }),
        ('Save Info', {
            'classes': ('collapse',),
            'fields': ('modified_by', 'modified', 'created',),
        }),
    )
    list_display  = (
        'watch',
        'type',
        'amount',
        'is_debit',
        'date',
    )
    ordering = ['-date',]
    readonly_fields = ('modified_by', 'modified', 'created',)

    def save_model(self, request, obj, form, change):
        obj.modified_by = request.user
        super().save_model(request, obj, form, change)
