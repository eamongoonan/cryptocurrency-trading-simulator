# Generated by Django 4.1.4 on 2023-02-21 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tradingplatform', '0008_position_pnl_position_roi_alter_platformuser_pnl_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='USD_value_of_sale',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
