from django.conf import settings
from django.db import models


class Value(models.Model):

    created = models.DateTimeField(
        auto_now_add=True,
        blank=False,
        null=False,
    )

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        models.PROTECT,
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

    is_debit = models.BooleanField(
        blank=False,
        null=False,
        default=False,
    )

    type = models.ForeignKey(
        'watches.ValueType',
        models.PROTECT,
        blank=False,
        null=False,
    )

    watch = models.ForeignKey(
        'watches.Watch',
        models.PROTECT,
        blank=True,
        null=True,
    )

    def __str__(self):
        return '{} | {} ${}'.format(self.id, self.type.name, self.amount,)
