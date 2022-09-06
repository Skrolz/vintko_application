from django.contrib import admin
from watch_list.models import Image


class ImageInline(admin.TabularInline):
    fields = ('created', 'file', 'is_visible',)
    extra = 1
    model = Image
    ordering = ['created',]
    readonly_fields = ['created',]
    show_change_link = True
