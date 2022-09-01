from django.contrib import admin
from watch_list.models import ValueType


class ValueTypeInline(admin.TabularInline):
    fields = ('name',)
    extra = 1
    model = ValueType
