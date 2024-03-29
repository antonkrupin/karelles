# Generated by Django 2.0.13 on 2019-08-28 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataset', '0014_auto_20190820_0806'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Имя')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Электронная почта')),
                ('phone', models.CharField(max_length=20, verbose_name='Телефон')),
            ],
            options={
                'verbose_name': 'Контактные данные заказчиков',
                'verbose_name_plural': 'Контактные данные заказчиков',
            },
        ),
    ]
