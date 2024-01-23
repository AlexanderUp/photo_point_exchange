from django.contrib import admin

from rates.models import CurrencyRate


class CurrencyRateAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'timestamp',
        'rate',
        'created_at',
    )


admin.site.register(CurrencyRate, CurrencyRateAdmin)
