# Generated by Django 2.2.12 on 2020-05-29 21:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('paper', '0057_figure_created_location'),
        ('discussion', '0022_externalcomment_externalreply_externalthread'),
    ]

    operations = [
        migrations.AddField(
            model_name='externalcomment',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='discussion.ExternalThread'),
        ),
        migrations.AddField(
            model_name='externalreply',
            name='content_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='externalreply',
            name='object_id',
            field=models.PositiveIntegerField(default=55),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='externalthread',
            name='paper',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='external_threads', to='paper.Paper'),
        ),
    ]
