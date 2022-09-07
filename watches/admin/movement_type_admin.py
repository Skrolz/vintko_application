from django.contrib import admin
from watches.models import MovementType


@admin.register(MovementType)
class MovementTypeAdmin(admin.ModelAdmin):
    fields = ('name',)
    list_display  = ('name',)
    ordering = ['name',]
