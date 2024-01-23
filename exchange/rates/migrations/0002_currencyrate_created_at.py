# Generated by Django 5.0.1 on 2024-01-23 10:46

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('rates', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='currencyrate',
            name='created_at',
            field=models.DateTimeField(
                default=django.utils.timezone.now,
                help_text='Entry created at',
                verbose_name='created_at',
            ),
        ),
    ]
