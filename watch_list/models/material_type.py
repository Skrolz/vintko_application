from django.db import models


class MaterialType(models.Model):

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

    def __str__(self):
        return '%s' % (self.name,)
