# Generated by Django 2.2.7 on 2019-11-25 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reputation', '0002_auto_20191017_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='distribution',
            name='distribution_type',
            field=models.CharField(choices=[('CREATE_PAPER', 'CREATE_PAPER'), ('COMMENT_ENDORSED', 'COMMENT_ENDORSED'), ('COMMENT_FLAGGED', 'COMMENT_FLAGGED'), ('COMMENT_UPVOTED', 'COMMENT_UPVOTED'), ('COMMENT_DOWNVOTED', 'COMMENT_DOWNVOTED'), ('REPLY_ENDORSED', 'REPLY_ENDORSED'), ('REPLY_FLAGGED', 'REPLY_FLAGGED'), ('REPLY_UPVOTED', 'REPLY_UPVOTED'), ('REPLY_DOWNVOTED', 'REPLY_DOWNVOTED'), ('THREAD_ENDORSED', 'THREAD_ENDORSED'), ('THREAD_FLAGGED', 'THREAD_FLAGGED'), ('THREAD_UPVOTED', 'THREAD_UPVOTED'), ('THREAD_DOWNVOTED', 'THREAD_DOWNVOTED')], max_length=255),
        ),
    ]
