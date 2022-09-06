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

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for obj in formset.deleted_objects:
            obj.delete()
        for instance in instances:
            instance.modified_by = request.user
            instance.save()
        formset.save_m2m()
