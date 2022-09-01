from django.contrib import admin
from watch_list.models import Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    fields = (
        'watch',
        'file',
        'description',
        'is_visible',
    )
    list_display  = (
        'watch',
        'file',
        'is_visible',
    )
