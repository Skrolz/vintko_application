from django.db import models
from . import Watch

class Image(models.Model):

    created = models.DateField(
        auto_now_add=True,
        blank=False,
        null=False,
    )

    modified = models.DateField(
        auto_now=True,
        blank=False,
        null=False,
    )

    description = models.TextField(
        blank=True,
        null=False,
        default="",
        max_length=2048,
    )

    file = models.FileField(
        blank=False,
        null=False,
        unique=True,
        upload_to='media',
    )

    is_visible = models.BooleanField(
        blank=False,
        null=False,
    )

    watch = models.ForeignKey(
        Watch,
        blank=False,
        null=False,
        on_delete=models.PROTECT,
    )
