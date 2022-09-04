from django.db import models
from resource.models import Country


class Brand(models.Model):

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

    country = models.ForeignKey(
        Country,
        blank=False,
        null=False,
        on_delete=models.PROTECT,
    )

    name = models.CharField(
        blank=False,
        null=False,
        max_length=64,
        unique=True,
    )

    def __str__(self):
        return '%s' % (self.name,)
