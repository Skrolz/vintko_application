from django.db import models


class Image(models.Model):

    created = models.DateTimeField(
        auto_now_add=True,
        blank=False,
        null=False,
    )

    modified = models.DateTimeField(
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
        'watch_list.Watch',
        models.PROTECT,
        blank=False,
        null=False,
    )
