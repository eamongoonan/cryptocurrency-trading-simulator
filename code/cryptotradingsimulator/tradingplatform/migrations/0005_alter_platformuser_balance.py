# Generated by Django 4.1.4 on 2023-02-18 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tradingplatform', '0004_rename_dollarvalueofsale_position_usd_value_of_sale_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='platformuser',
            name='balance',
            field=models.PositiveIntegerField(default=7000),
        ),
    ]