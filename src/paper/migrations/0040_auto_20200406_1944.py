# Generated by Django 2.2.11 on 2020-04-06 19:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paper', '0039_auto_20200402_2319'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paper',
            old_name='tagline',
            new_name='abstract',
        ),
    ]