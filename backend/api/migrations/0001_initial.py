# Generated by Django 5.0.6 on 2024-07-09 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CurrencyRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата выполнения запроса')),
                ('origin_currency', models.CharField(default='USD', max_length=3, verbose_name='Наименование исходной валюты')),
                ('target_currency', models.CharField(default='RUB', max_length=3, verbose_name='Наименование результирующей валюты')),
                ('rate', models.FloatField(null=True, verbose_name='Курс (по данным ЦБ РФ)')),
            ],
            options={
                'verbose_name': 'Запрос валютного курса',
                'verbose_name_plural': 'Запросы валютного курса',
                'ordering': ('-created_at',),
            },
        ),
    ]
