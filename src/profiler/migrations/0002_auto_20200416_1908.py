# Generated by Django 2.2.12 on 2020-04-16 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiler', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='traceback',
            name='trace',
            field=models.FileField(blank=True, default=None, null=True, upload_to='uploads/traceback/%Y/%m/%d'),
        ),
    ]
