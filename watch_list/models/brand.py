from django.db import models
from resource.models import Country


class Brand(models.Model):
    country = models.ForeignKey(
        Country,
        blank=False,
        null=False,
        on_delete=models.CASCADE,
    )

    name = models.CharField(
        blank=False,
        null=False,
        max_length=64,
        unique=True,
    )

    def __str__(self):
        return '%s' % (self.name,)
