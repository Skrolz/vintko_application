from django.db import models
from . import ValueType, Watch

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
        max_digits=8
    )

    date = models.DateField(
        blank=True,
        null=True,
    )

    description = models.TextField(
        blank=True,
        null=False,
        default="",
        max_length=2048
    )

    type = models.ForeignKey(
        ValueType,
        blank=False,
        null=False,
        on_delete=models.PROTECT
    )

    watch = models.ForeignKey(
        Watch,
        blank=True,
        null=True,
        on_delete=models.PROTECT,
    )
