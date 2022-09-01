from django.contrib import admin
from watch_list.models import Value


class ValueInline(admin.TabularInline):
    fields = ('type', 'description', 'amount',)
    extra = 1
    model = Value
