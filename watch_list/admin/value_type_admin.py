from django.contrib import admin
from watch_list.models import ValueType


@admin.register(ValueType)
class ValueTypeAdmin(admin.ModelAdmin):
    fields = ('name',)
    list_display  = ('name',)
