from django.contrib import admin
from watches.models import ValueType
from watches.inlines import ValueInline


@admin.register(ValueType)
class ValueTypeAdmin(admin.ModelAdmin):
    fields = ('name', 'total_value',)
    inlines = [ValueInline,]
    list_display  = ('name',)
    ordering = ['name',]
    readonly_fields = ['total_value',]

    def get_readonly_fields(self, request, obj=None):
        if not request.user.is_superuser:
            return [f.name for f in self.model._meta.fields]
        return self.readonly_fields

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for obj in formset.deleted_objects:
            obj.delete()
        for instance in instances:
            if instance.id is None:
                instance.created_by = request.user
            instance.save()
        formset.save_m2m()
