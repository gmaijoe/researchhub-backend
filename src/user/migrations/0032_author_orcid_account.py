# Generated by Django 2.2.10 on 2020-03-03 22:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('socialaccount', '0003_extra_data_default_dict'),
        ('user', '0031_auto_20200219_2004'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='orcid_account',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='socialaccount.SocialAccount'),
        ),
    ]
