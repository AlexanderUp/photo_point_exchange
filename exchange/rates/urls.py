from django.urls import path

from rates.views import USDExchangeView

app_name = 'rates'

urlpatterns = [
    path('get-current-usd', USDExchangeView.as_view(), name='get_current_usd'),
]
