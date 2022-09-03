from django.contrib import admin
from watch_list.models import MaterialType


class MaterialTypeInline(admin.TabularInline):
    fields = ('name',)
    extra = 1
    model = MaterialType
