# Generated by Django 2.2 on 2020-11-14 02:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paper', '0068_paper_sift_risk_score'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paper',
            name='sift_risk_score',
        ),
    ]
