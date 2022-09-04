from django.contrib import admin
from watch_list.models import MovementType


@admin.register(MovementType)
class MovementTypeAdmin(admin.ModelAdmin):
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
