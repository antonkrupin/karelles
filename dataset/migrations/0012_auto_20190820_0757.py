# Generated by Django 2.0.13 on 2019-08-20 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataset', '0011_auto_20190820_0756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price_300',
            name='price',
            field=models.DecimalField(decimal_places=0, max_digits=4, verbose_name='Стоимость'),
        ),
    ]
