# Generated by Django 2.2.5 on 2019-09-20 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hub', '0001_initial'),
        ('user', '0002_author_university'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('uploaded_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('paper_publish_date', models.DateField()),
                ('doi', models.CharField(blank=True, default='', max_length=255)),
                ('url', models.URLField(blank=True, default='')),
                ('authors', models.ManyToManyField(blank=True, related_name='authored_papers', to='user.Author')),
                ('hubs', models.ManyToManyField(blank=True, related_name='papers', to='hub.Hub')),
            ],
        ),
    ]
