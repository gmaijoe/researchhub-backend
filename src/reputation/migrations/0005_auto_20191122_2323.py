# Generated by Django 2.2.7 on 2019-11-22 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reputation', '0004_auto_20191122_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='distribution',
            name='is_removed_date',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='withdrawal',
            name='is_removed_date',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]
