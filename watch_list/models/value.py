from django.db import models
from . import ValueType, Watch

class Value(models.Model):
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
        null=True,
        max_length=2048
    )

    type = models.ForeignKey(
        ValueType,
        blank=False,
        null=False,
        on_delete=models.CASCADE
    )

    watch = models.ForeignKey(
        Watch,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )
