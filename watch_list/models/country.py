from django.db import models


class Country(models.Model):

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

    name = models.CharField(
        blank=False,
        null=False,
        max_length=64,
        unique=True,
    )

    class Meta:
        verbose_name_plural = "countries"

    def __str__(self):
        return '{}'.format(self.name,)
