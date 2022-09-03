from django.contrib import admin
from watch_list.models import MovementType


class MovementTypeInline(admin.TabularInline):
    fields = ('name',)
    extra = 1
    model = MovementType
