from django.contrib import admin
from watch_list.models import MovementType


@admin.register(MovementType)
class MovementTypeAdmin(admin.ModelAdmin):
    fields = ('name',)
    list_display  = ('name',)
