# Generated by Django 2.0.13 on 2019-08-20 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataset', '0005_auto_20190820_0737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='il_1',
            name='about',
            field=models.CharField(max_length=400, verbose_name='Название отчета'),
        ),
    ]