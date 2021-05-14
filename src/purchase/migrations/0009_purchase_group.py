# Generated by Django 2.2.13 on 2020-07-14 00:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0008_aggregatepurchase'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='purchases', to='purchase.AggregatePurchase'),
        ),
    ]