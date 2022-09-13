from django.db import models
from django.utils.safestring import mark_safe
from watches.models.value import Value


class ValueType(models.Model):

    name = models.CharField(
        blank=False,
        null=False,
        max_length=64,
        unique=True,
    )

    def __str__(self):
        return '{}'.format(self.name,)

    @mark_safe
    def total_value(self):
        total = 0
        values = Value.objects.filter(type=self)
        for value in values:
            if value.is_debit:
                total -= value.amount
            else:
                total += value.amount
        if total > 0:
            return '<span style="color:#ffcccc;">${} spent</span>'.format(total,)
        else:
            return '<span style="color:#ccffcc;">${} earned</span>'.format(-total,)
