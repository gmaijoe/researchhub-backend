# Generated by Django 2.2.11 on 2020-03-17 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paper', '0032_auto_20200316_2355'),
    ]

    operations = [
        migrations.AddField(
            model_name='figure',
            name='figure_type',
            field=models.CharField(choices=[('FIGURE', 'Figure'), ('PREVIEW', 'Preview')], default='FIGURE', max_length=16),
            preserve_default=False,
        ),
    ]