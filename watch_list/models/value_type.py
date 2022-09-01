from django.db import models

class ValueType(models.Model):
    name = models.CharField(
        blank=False,
        null=False,
        max_length=64,
        unique=True,
    )

    def __str__(self):
        return '%s' % (self.name,)
