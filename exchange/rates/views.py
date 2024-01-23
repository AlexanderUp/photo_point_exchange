from django.http import JsonResponse
from django.views import View

from rates.services import get_last_rates


class USDExchangeView(View):
    def get(self, request, *args, **kwargs):
        rates = get_last_rates()
        return JsonResponse(rates, safe=False)
