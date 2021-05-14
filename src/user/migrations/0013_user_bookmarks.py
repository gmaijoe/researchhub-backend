# Generated by Django 2.2.7 on 2019-11-12 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paper', '0014_auto_20191109_0601'),
        ('user', '0012_auto_20191109_0601'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='bookmarks',
            field=models.ManyToManyField(related_name='users_who_bookmarked', to='paper.Paper'),
        ),
    ]