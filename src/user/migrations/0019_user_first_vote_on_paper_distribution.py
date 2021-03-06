# Generated by Django 2.2.8 on 2019-12-11 20:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reputation', '0012_auto_20191210_1921'),
        ('user', '0018_user_has_seen_first_vote_modal'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='first_vote_on_paper_distribution',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='reputation.Distribution'),
        ),
    ]
