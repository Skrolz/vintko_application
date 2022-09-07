from django.contrib import admin
from watch_list.models import Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': (
                'file',
                'watch',
                'description',
                'is_visible',
            )
        }),
        ('Save info', {
            'classes': ('collapse',),
            'fields': ('modified', 'created',),
        }),
    )
    list_display  = (
        'watch',
        'file',
        'is_visible',
    )
    ordering = ['watch',]
    readonly_fields = ('modified', 'created',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(watch__created_by=request.user)
