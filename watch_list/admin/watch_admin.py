from django.contrib import admin
from watch_list.models import Watch
from watch_list.inlines import ImageInline, ValueInline


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
            'fields': ('modified_by', 'modified', 'created'),
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
    readonly_fields = ('modified_by', 'modified', 'created',)

    def save_model(self, request, obj, form, change):
        obj.modified_by = request.user
        super().save_model(request, obj, form, change)

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for obj in formset.deleted_objects:
            obj.delete()
        for instance in instances:
            instance.modified_by = request.user
            instance.save()
        formset.save_m2m()
