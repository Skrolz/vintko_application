from django.db import models


class Country(models.Model):
    name = models.CharField(
        blank=False,
        null=False,
        max_length=64,
        unique=True,
    )

    class Meta:
        verbose_name_plural = "countries"

    def __str__(self):
        return '%s' % (self.name,)
