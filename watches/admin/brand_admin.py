from django.contrib import admin
from watches.models import Brand
from watches.inlines import WatchInline


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
