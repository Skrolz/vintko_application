from django.contrib import admin
from watch_list.models import Image


class ImageInline(admin.TabularInline):
    fields = ('file', 'is_visible',)
    extra = 1
    model = Image
