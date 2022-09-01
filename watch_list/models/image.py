from django.db import models
from . import Watch

class Image(models.Model):
    description = models.TextField(
        blank=True,
        null=True,
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
        on_delete=models.CASCADE,
    )
