# Generated by Django 2.2 on 2020-10-20 22:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0042_auto_20201007_0025'),
        ('purchase', '0012_auto_20201006_2251'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wallet',
            name='user',
        ),
        migrations.AddField(
            model_name='wallet',
            name='author',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='wallet', to='user.Author'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='wallet',
            name='btc_address',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='eth_address',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='rsc_address',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
