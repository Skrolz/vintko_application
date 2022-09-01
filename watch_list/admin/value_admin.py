from django.contrib import admin
from watch_list.models import Value


@admin.register(Value)
class ValueAdmin(admin.ModelAdmin):
    fields = (
        'watch',
        'type',
        'amount',
        'date',
    )
    list_display  = (
        'watch',
        'type',
        'amount',
        'date',
    )
