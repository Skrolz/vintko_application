# Generated by Django 4.1.1 on 2022-09-08 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watches', '0003_remove_watch_is_visible'),
    ]

    operations = [
        migrations.AlterField(
            model_name='value',
            name='description',
            field=models.CharField(blank=True, default='', max_length=1024),
        ),
    ]
