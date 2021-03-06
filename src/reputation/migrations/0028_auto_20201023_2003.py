# Generated by Django 2.2 on 2020-10-23 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reputation', '0027_auto_20200819_2338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='distribution',
            name='distribution_type',
            field=models.CharField(choices=[('FLAG_PAPER', 'FLAG_PAPER'), ('PAPER_UPVOTED', 'PAPER_UPVOTED'), ('CREATE_BULLET_POINT', 'CREATE_BULLET_POINT'), ('BULLET_POINT_FLAGGED', 'BULLET_POINT_FLAGGED'), ('COMMENT_CENSORED', 'COMMENT_CENSORED'), ('COMMENT_FLAGGED', 'COMMENT_FLAGGED'), ('COMMENT_UPVOTED', 'COMMENT_UPVOTED'), ('COMMENT_DOWNVOTED', 'COMMENT_DOWNVOTED'), ('REPLY_CENSORED', 'REPLY_CENSORED'), ('REPLY_FLAGGED', 'REPLY_FLAGGED'), ('REPLY_UPVOTED', 'REPLY_UPVOTED'), ('REPLY_DOWNVOTED', 'REPLY_DOWNVOTED'), ('THREAD_CENSORED', 'THREAD_CENSORED'), ('THREAD_FLAGGED', 'THREAD_FLAGGED'), ('THREAD_UPVOTED', 'THREAD_UPVOTED'), ('THREAD_DOWNVOTED', 'THREAD_DOWNVOTED'), ('CREATE_SUMMARY', 'CREATE_SUMMARY'), ('REFERRAL', 'REFERRAL')], max_length=255),
        ),
    ]
