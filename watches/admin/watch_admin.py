from django.contrib import admin
from watches.models import Watch
from watches.inlines import ValueInline


@admin.register(Watch)
class WatchAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': (
                'year',
                'brand',
                ('model',
                'reference_number',
                'serial_number',),
                'movement_type',
                ('case_material',
                'band_material',
                'dial_description',),
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
            'fields': ('created_by', 'created', 'modified',),
        }),
    )
    inlines = [ValueInline,]
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
    readonly_fields = ('created_by', 'created', 'modified',)

    def save_model(self, request, obj, form, change):
        if obj.id is None:
            obj.created_by = request.user
        super().save_model(request, obj, form, change)

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for obj in formset.deleted_objects:
            obj.delete()
        for instance in instances:
            if instance.id is None:
                instance.created_by = request.user
            instance.save()
        formset.save_m2m()

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(created_by=request.user)
