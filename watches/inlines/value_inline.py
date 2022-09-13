from django.contrib import admin
from watches.models import Value


class ValueInline(admin.StackedInline):
    fields = ('date', 'type', ('amount', 'is_debit',), 'description', 'watch',)
    extra = 1
    model = Value
    ordering = ['-date',]
    show_change_link = True
