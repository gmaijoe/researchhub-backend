# Generated by Django 2.2.9 on 2020-01-10 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0022_action'),
    ]

    operations = [
        migrations.AddField(
            model_name='action',
            name='read_date',
            field=models.DateTimeField(default=None, null=True),
        ),
    ]
