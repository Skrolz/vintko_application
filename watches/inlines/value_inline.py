from django.contrib import admin
from watches.models import Value


class ValueInline(admin.TabularInline):
    fields = ('date', 'type', 'description', 'amount', 'is_debit',)
    extra = 1
    model = Value
    ordering = ['-date',]
    show_change_link = True