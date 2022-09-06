from django.contrib import admin
from watch_list.models import ValueType
from watch_list.inlines import ValueInline


@admin.register(ValueType)
class ValueTypeAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('name',)
        }),
        ('Save Info', {
            'classes': ('collapse',),
            'fields': ('modified', 'created',),
        }),
    )
    inlines = [ValueInline,]
    list_display  = ('name',)
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
