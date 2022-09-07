from django.contrib import admin
from watches.models import Brand


class BrandInline(admin.TabularInline):
    fields = ('name',)
    extra = 1
    model = Brand
    ordering = ['name',]
