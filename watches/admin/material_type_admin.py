from django.contrib import admin
from watches.models import MaterialType


@admin.register(MaterialType)
class MaterialTypeAdmin(admin.ModelAdmin):
    fields = ('name',)
    list_display  = ('name',)
    ordering = ['name',]
