# Generated by Django 4.1.4 on 2023-02-13 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tradingplatform', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='position',
            old_name='dollarValueAtPurchase',
            new_name='dollarValueOfPurchase',
        ),
        migrations.RenameField(
            model_name='position',
            old_name='dollarValueAtSale',
            new_name='dollarValueOfSale',
        ),
    ]
