# Generated by Django 2.2 on 2021-03-31 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discussion', '0031_auto_20210312_2048'),
    ]

    operations = [
        migrations.AddField(
            model_name='thread',
            name='block_key',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='thread',
            name='entity_key',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
