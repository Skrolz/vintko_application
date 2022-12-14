from django.db import models


class Brand(models.Model):

    country = models.ForeignKey(
        'watches.Country',
        models.PROTECT,
        blank=False,
        null=False,
    )

    name = models.CharField(
        blank=False,
        null=False,
        max_length=64,
        unique=True,
    )

    def __str__(self):
        return '{}'.format(self.name,)
