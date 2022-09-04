# Generated by Django 4.1 on 2022-09-04 22:38

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('resource', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=64, unique=True)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='resource.country')),
            ],
        ),
        migrations.CreateModel(
            name='MaterialType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=64, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='MovementType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=64, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ValueType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=64, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Watch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('case_thickness', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(2), django.core.validators.MaxValueValidator(128)])),
                ('case_width', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(2), django.core.validators.MaxValueValidator(128)])),
                ('dial_description', models.CharField(blank=True, default='', max_length=512)),
                ('description', models.TextField(blank=True, default='', max_length=2048)),
                ('is_visible', models.BooleanField()),
                ('lug_to_lug', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(2), django.core.validators.MaxValueValidator(128)])),
                ('lug_width', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(2), django.core.validators.MaxValueValidator(128)])),
                ('model', models.CharField(blank=True, default='', max_length=64)),
                ('reference_number', models.CharField(blank=True, default='', max_length=64)),
                ('serial_number', models.CharField(blank=True, default='', max_length=64)),
                ('year', models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1024), django.core.validators.MaxValueValidator(2048)])),
                ('band_material', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='watch_band_material_type', to='watch_list.materialtype')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='watch_list.brand')),
                ('case_material', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='watch_list.materialtype')),
                ('movement_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='watch_list.movementtype')),
            ],
            options={
                'verbose_name_plural': 'watches',
            },
        ),
        migrations.CreateModel(
            name='Value',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=8)),
                ('date', models.DateField(blank=True, null=True)),
                ('description', models.TextField(blank=True, default='', max_length=2048)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='watch_list.valuetype')),
                ('watch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='watch_list.watch')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('description', models.TextField(blank=True, default='', max_length=2048)),
                ('file', models.FileField(unique=True, upload_to='media')),
                ('is_visible', models.BooleanField()),
                ('watch', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='watch_list.watch')),
            ],
        ),
    ]
