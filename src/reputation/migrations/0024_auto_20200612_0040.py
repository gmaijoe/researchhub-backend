# Generated by Django 2.2.13 on 2020-06-12 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reputation', '0023_auto_20200610_2236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='distribution',
            name='distribution_type',
            field=models.CharField(choices=[('SIGN_UP', 'SIGN_UP'), ('CREATE_PAPER', 'CREATE_PAPER'), ('VOTE_ON_PAPER', 'VOTE_ON_PAPER'), ('CREATE_BULLET_POINT', 'CREATE_BULLET_POINT'), ('BULLET_POINT_ENDORSED', 'BULLET_POINT_ENDORSED'), ('BULLET_POINT_FLAGGED', 'BULLET_POINT_FLAGGED'), ('CREATE_COMMENT', 'CREATE_COMMENT'), ('VOTE_ON_COMMENT', 'VOTE_ON_COMMENT'), ('COMMENT_ENDORSED', 'COMMENT_ENDORSED'), ('COMMENT_FLAGGED', 'COMMENT_FLAGGED'), ('COMMENT_UPVOTED', 'COMMENT_UPVOTED'), ('COMMENT_DOWNVOTED', 'COMMENT_DOWNVOTED'), ('CREATE_REPLY', 'CREATE_REPLY'), ('VOTE_ON_REPLY', 'VOTE_ON_REPLY'), ('REPLY_ENDORSED', 'REPLY_ENDORSED'), ('REPLY_FLAGGED', 'REPLY_FLAGGED'), ('REPLY_UPVOTED', 'REPLY_UPVOTED'), ('REPLY_DOWNVOTED', 'REPLY_DOWNVOTED'), ('CREATE_THREAD', 'CREATE_THREAD'), ('VOTE_ON_THREAD', 'VOTE_ON_THREAD'), ('THREAD_ENDORSED', 'THREAD_ENDORSED'), ('THREAD_FLAGGED', 'THREAD_FLAGGED'), ('THREAD_UPVOTED', 'THREAD_UPVOTED'), ('THREAD_DOWNVOTED', 'THREAD_DOWNVOTED'), ('CREATE_SUMMARY', 'CREATE_SUMMARY')], max_length=255),
        ),
    ]
