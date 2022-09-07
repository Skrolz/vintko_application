from django.contrib import admin
from watches.models import Country
from watches.inlines import BrandInline


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    fields = ('name',)
    inlines = [BrandInline,]
    list_display  = ('name',)
    ordering = ['name',]
