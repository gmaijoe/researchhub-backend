# Generated by Django 2.2 on 2020-11-04 22:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('discussion', '0026_auto_20200623_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='discussion_votes', to=settings.AUTH_USER_MODEL),
        ),
    ]
