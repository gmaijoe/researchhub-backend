# Generated by Django 2.2 on 2021-03-10 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paper', '0074_paper_external_metadata'),
    ]

    operations = [
        migrations.AddField(
            model_name='paper',
            name='twitter_score_updated_date',
            field=models.DateTimeField(null=True),
        ),
    ]
