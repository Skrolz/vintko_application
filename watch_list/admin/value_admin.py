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
            'fields': ('created_by', 'created', 'modified',),
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
    readonly_fields = ('created_by', 'created', 'modified',)

    def save_model(self, request, obj, form, change):
        if obj.id is None:
            obj.created_by = request.user
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(created_by=request.user)
