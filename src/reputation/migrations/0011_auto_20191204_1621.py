# Generated by Django 2.2.8 on 2019-12-04 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reputation', '0010_auto_20191204_1515'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='withdrawal',
            name='amount_decimal_part',
        ),
        migrations.RemoveField(
            model_name='withdrawal',
            name='amount_integer_part',
        ),
    ]
