# Generated by Django 2.2.9 on 2020-02-14 00:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('summary', '0007_summary_summary_plain_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='summary',
            name='approved_by',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='approved', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='summary',
            name='paper',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='summaries', to='paper.Paper'),
        ),
        migrations.AlterField(
            model_name='summary',
            name='previous',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='next', to='summary.Summary'),
        ),
        migrations.AlterField(
            model_name='summary',
            name='proposed_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='edits', to=settings.AUTH_USER_MODEL),
        ),
    ]
