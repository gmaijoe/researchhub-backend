# Generated by Django 2.2.8 on 2019-12-10 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reputation', '0011_auto_20191204_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='distribution',
            name='distribution_type',
            field=models.CharField(choices=[('CREATE_PAPER', 'CREATE_PAPER'), ('VOTE_ON_PAPER', 'VOTE_ON_PAPER'), ('COMMENT_ENDORSED', 'COMMENT_ENDORSED'), ('COMMENT_FLAGGED', 'COMMENT_FLAGGED'), ('COMMENT_UPVOTED', 'COMMENT_UPVOTED'), ('COMMENT_DOWNVOTED', 'COMMENT_DOWNVOTED'), ('REPLY_ENDORSED', 'REPLY_ENDORSED'), ('REPLY_FLAGGED', 'REPLY_FLAGGED'), ('REPLY_UPVOTED', 'REPLY_UPVOTED'), ('REPLY_DOWNVOTED', 'REPLY_DOWNVOTED'), ('THREAD_ENDORSED', 'THREAD_ENDORSED'), ('THREAD_FLAGGED', 'THREAD_FLAGGED'), ('THREAD_UPVOTED', 'THREAD_UPVOTED'), ('THREAD_DOWNVOTED', 'THREAD_DOWNVOTED')], max_length=255),
        ),
        migrations.AddConstraint(
            model_name='distribution',
            constraint=models.UniqueConstraint(condition=models.Q(distribution_type='VOTE_ON_PAPER'), fields=('recipient', 'distribution_type'), name='recipient_vote_on_paper'),
        ),
    ]
