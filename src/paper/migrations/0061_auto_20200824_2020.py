# Generated by Django 2.2.15 on 2020-08-24 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paper', '0060_auto_20200721_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metadataretrievalattempt',
            name='method',
            field=models.CharField(choices=[('CROSSREF_DOI', 'CROSSREF_DOI'), ('CROSSREF_QUERY', 'CROSSREF_QUERY'), ('MANUBOT_DOI', 'MANUBOT_DOI'), ('MANUBOT_PDF_URL', 'MANUBOT_PDF_URL'), ('MANUBOT_URL', 'MANUBOT_URL'), ('PARSE_PDF', 'PARSE_PDF'), ('PDF_FROM_URL', 'PDF_FROM_URL')], max_length=125),
        ),
    ]
