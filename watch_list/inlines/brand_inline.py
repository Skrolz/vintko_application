from django.contrib import admin
from watch_list.models import Brand


class BrandInline(admin.TabularInline):
    fields = ('name',)
    extra = 1
    model = Brand
