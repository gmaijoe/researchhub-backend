# Generated by Django 2.2.8 on 2020-01-16 23:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hub', '0006_hub_acronym'),
        ('user', '0023_action_read_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='action',
            name='hub',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='actions', to='hub.Hub'),
        ),
    ]
