# Generated by Django 2.2 on 2020-11-20 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paper', '0070_paper_is_removed_by_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='paper',
            name='bullet_low_quality',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='paper',
            name='summary_low_quality',
            field=models.BooleanField(default=True),
        ),
    ]
