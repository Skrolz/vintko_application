from django.contrib import admin
from watch_list.models import MaterialType


@admin.register(MaterialType)
class MaterialTypeAdmin(admin.ModelAdmin):
    fields = ('name',)
    list_display  = ('name',)
