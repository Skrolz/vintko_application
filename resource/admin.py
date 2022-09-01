from django.contrib import admin
from .models import Country
from watch_list.inlines import BrandInline


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    fields = ('name',)
    inlines = [BrandInline,]
    list_display  = ('name',)
