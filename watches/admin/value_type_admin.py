from django.contrib import admin
from watches.models import ValueType
from watches.inlines import ValueInline


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

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return self.readonly_fields
        return [f.name for f in self.model._meta.fields]

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for obj in formset.deleted_objects:
            obj.delete()
        for instance in instances:
            if instance.id is None:
                instance.created_by = request.user
            instance.save()
        formset.save_m2m()
