# Generated by Django 2.2.7 on 2019-11-09 06:01

from django.db import migrations, models
import user.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_auto_20191104_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='profile_image',
            field=models.FileField(blank=True, default=None, null=True, storage=user.models.ProfileImageStorage(), upload_to='uploads/author_profile_images/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='user',
            name='reputation',
            field=models.IntegerField(default=100),
        ),
    ]
