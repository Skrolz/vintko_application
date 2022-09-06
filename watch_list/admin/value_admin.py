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

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for obj in formset.deleted_objects:
            obj.delete()
        for instance in instances:
            instance.modified_by = request.user
            instance.save()
        formset.save_m2m()
