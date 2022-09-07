from django.contrib import admin
from watches.models import Country
from watches.inlines import BrandInline


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('name',)
        }),
        ('Save info', {
            'classes': ('collapse',),
            'fields': ('modified', 'created',),
        }),
    )
    inlines = [BrandInline,]
    list_display  = ('name',)
    ordering = ['name',]
    readonly_fields = ('modified', 'created',)
