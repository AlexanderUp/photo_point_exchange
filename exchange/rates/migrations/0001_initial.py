# Generated by Django 5.0.1 on 2024-01-23 08:34

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies: list = []

    operations = [
        migrations.CreateModel(
            name='CurrencyRate',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'timestamp',
                    models.DateTimeField(
                        help_text='Timestamp', verbose_name='timestamp'
                    ),
                ),
                (
                    'rate',
                    models.DecimalField(
                        decimal_places=4,
                        help_text='Currency rate',
                        max_digits=7,
                        verbose_name='rate',
                    ),
                ),
            ],
            options={
                'verbose_name': 'Currency Rate',
                'verbose_name_plural': 'Currency Rates',
                'ordering': ('-timestamp',),
            },
        ),
    ]