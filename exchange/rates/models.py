from django.db import models
from django.utils import timezone


class CurrencyRate(models.Model):
    timestamp = models.DateTimeField(
        verbose_name='timestamp',
        help_text='Timestamp',
    )
    rate = models.DecimalField(
        max_digits=7,
        decimal_places=4,
        verbose_name='rate',
        help_text='Currency rate',
    )
    created_at = models.DateTimeField(
        default=timezone.now,
        verbose_name='created_at',
        help_text='Entry created at',
    )

    class Meta:
        verbose_name = 'Currency Rate'
        verbose_name_plural = 'Currency Rates'
        ordering = ('-pk',)

    def __str__(self):
        return f'{self.timestamp}:{self.rate}'
