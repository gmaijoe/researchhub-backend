# Generated by Django 2.2.12 on 2020-05-12 22:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paper', '0055_auto_20200511_1555'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paper',
            name='external_source_id',
        ),
    ]
