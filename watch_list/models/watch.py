from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from . import Brand, MovementType

class Watch(models.Model):
    band_material = models.CharField(
        blank=True,
        null=True,
        max_length=64,
    )

    brand = models.ForeignKey(
        Brand,
        blank=False,
        null=False,
        on_delete=models.CASCADE,
    )

    case_material = models.CharField(
        blank=True,
        null=True,
        max_length=64,
    )

    case_thickness = models.PositiveIntegerField(
        blank=True,
        null=True,
        validators=[
            MinValueValidator(2),
            MaxValueValidator(128)
        ],
    )

    case_width = models.PositiveIntegerField(
        blank=True,
        null=True,
        validators=[
            MinValueValidator(2),
            MaxValueValidator(128)
        ],
    )

    dial_description = models.CharField(
        blank=True,
        null=True,
        max_length=512,
    )

    description = models.TextField(
        blank=True,
        null=True,
        max_length=2048,
    )

    is_visible = models.BooleanField(
        blank=False,
        null=False,
    )

    lug_to_lug = models.PositiveIntegerField(
        blank=True,
        null=True,
        validators=[
            MinValueValidator(2),
            MaxValueValidator(128)
        ]
    )

    lug_width = models.PositiveIntegerField(
        blank=True,
        null=True,
        validators=[
            MinValueValidator(2),
            MaxValueValidator(128)
        ]
    )

    model = models.CharField(
        blank=True,
        null=True,
        max_length=64,
    )

    movement_type = models.ForeignKey(
        MovementType,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )

    reference_number = models.CharField(
        blank=True,
        null=True,
        max_length=64,
    )

    year = models.PositiveSmallIntegerField(
        blank=True,
        null=True,
        validators=[
            MinValueValidator(1024),
            MaxValueValidator(2048)
        ],
    )

    def __str__(self):
        return '%s %s %s' % (self.year, self.brand, self.model,)

    class Meta:
        verbose_name_plural = "watches"
