from django.contrib import admin
from watch_list.models import MaterialType


@admin.register(MaterialType)
class MaterialTypeAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('name',)
        }),
        ('Save Info', {
            'classes': ('collapse',),
            'fields': ('modified', 'created',),
        }),
    )
    list_display  = ('name',)
    ordering = ['name',]
    readonly_fields = ('modified', 'created',)
