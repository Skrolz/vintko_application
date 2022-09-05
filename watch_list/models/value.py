from django.db import models


class Value(models.Model):

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

    amount = models.DecimalField(
        blank=False,
        null=False,
        decimal_places=2,
        default=0.00,
        max_digits=8,
    )

    date = models.DateField(
        blank=True,
        null=True,
    )

    description = models.TextField(
        blank=True,
        null=False,
        default="",
        max_length=2048,
    )

    type = models.ForeignKey(
        'watch_list.ValueType',
        models.PROTECT,
        blank=False,
        null=False,
    )

    watch = models.ForeignKey(
        'watch_list.Watch',
        models.PROTECT,
        blank=True,
        null=True,
    )
