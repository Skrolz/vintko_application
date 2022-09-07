from datetime import date
from django.conf import settings
from django.db import models


class Watch(models.Model):

    MM_CHOICES = [(i,i) for i in range(5,65)]
    YEAR_CHOICES = [(i,i) for i in range(1900,date.today().year+2)]

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

    band_material = models.ForeignKey(
        'watches.MaterialType',
        models.PROTECT,
        blank=True,
        null=True,
        related_name='watch_band_material_type'
    )

    brand = models.ForeignKey(
        'watches.Brand',
        models.PROTECT,
        blank=False,
        null=False,
    )

    case_material = models.ForeignKey(
        'watches.MaterialType',
        models.PROTECT,
        blank=True,
        null=True,
    )

    case_thickness = models.IntegerField(
        blank=True,
        null=True,
        choices=MM_CHOICES
    )

    case_width = models.IntegerField(
        blank=True,
        null=True,
        choices=MM_CHOICES
    )

    description = models.TextField(
        blank=True,
        null=False,
        default="",
        max_length=2048,
    )

    dial_description = models.CharField(
        blank=True,
        null=False,
        default="",
        max_length=512,
    )

    is_visible = models.BooleanField(
        blank=False,
        null=False,
        default=False,
    )

    lug_to_lug = models.IntegerField(
        blank=True,
        null=True,
        choices=MM_CHOICES
    )

    lug_width = models.IntegerField(
        blank=True,
        null=True,
        choices=MM_CHOICES
    )

    model = models.CharField(
        blank=True,
        null=False,
        default="",
        max_length=64,
    )

    movement_type = models.ForeignKey(
        'watches.MovementType',
        models.PROTECT,
        blank=True,
        null=True,
    )

    reference_number = models.CharField(
        blank=True,
        null=False,
        default="",
        max_length=64,
    )

    serial_number = models.CharField(
        blank=True,
        null=False,
        default="",
        max_length=64,
    )

    year = models.IntegerField(
        blank=True,
        null=True,
        choices=YEAR_CHOICES
    )

    class Meta:
        verbose_name_plural = "watches"

    def __str__(self):
        return '{} | {} {} {}'.format(self.id, self.year or '', self.brand, self.reference_number or '',)
